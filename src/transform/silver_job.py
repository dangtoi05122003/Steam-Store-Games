from config.spark_session import get_spark
from config import setting
import pyspark.sql.functions as F
from utils import load_yaml, get_logger

logger = get_logger(__name__)

class Silver:
    def __init__(self, path):
        self.spark = get_spark()
        self.config = load_yaml(path)

    def get_table(self):
        for table_name in self.config['table']:
            logger.info(table_name)
            table_config = self.config['table'][table_name]
            schema = table_config['schema']
            df = self.spark.read.parquet(f"s3a://{setting.bucket_name}/bronze/{table_name}")
            cast_exprs = [F.col(c).cast(schema[c]).alias(c) if c in schema else F.col(f"`{c}`") for c in df.columns]
            df = df.select(*cast_exprs)
            processes = table_config.get('process', [])
            if processes:
                for step in processes:
                    df = self.execute_action(df, step)
            df.write.mode("overwrite").parquet(f"s3a://{setting.bucket_name}/silver/{table_name}")
    def execute_action(self, df, step):
        if not isinstance(step, dict):
            return df
        if "extract_regex" in step:
            inputs = step["extract_regex"]["inputs"]
            for target_col, config in inputs.items():
                df = df.withColumn(target_col, F.regexp_extract(F.col(config["source"]), config["pattern"], config.get("group", 1)))
        elif "clean_text_columns" in step:
            clean_config = step["clean_text_columns"]
            suffix = clean_config.get("source_suffix", "")
            for target in clean_config["targets"]:
                source_col = f"{target}{suffix}" if suffix else target
                cleaned_expr = F.col(source_col)
                for rep in clean_config["replacements"]:
                    cleaned_expr = F.regexp_replace(cleaned_expr, rep["pattern"], rep["replacement"])
                if clean_config.get("trim", False):
                    cleaned_expr = F.trim(cleaned_expr)
                if clean_config.get("null_if_empty", False):
                    cleaned_expr = F.when(F.col(source_col) == "", F.lit(None)).otherwise(cleaned_expr)
                df = df.withColumn(target, cleaned_expr)
        elif "drop_columns" in step:
            drop_cfg  = step["drop_columns"]
            df = df.drop(*drop_cfg)
        elif "calculations" in step:
            for new_col, expr in step["calculations"].items():
                df = df.withColumn(new_col, F.expr(expr))
        elif "filter_column" in step:
            config = step["filter_column"]
            ignore_column = config.get("ignore")
            output_column = config["output_column"]
            min_value = config["min_value"]
            tag_columns = [c for c in df.columns if c != ignore_column]
            tag_map = F.map_filter(
                F.map_from_arrays(
                    F.array(*[F.lit(c) for c in tag_columns]),
                    F.array(*[F.col(f"`{c}`").cast("long") for c in tag_columns])
                ),
                lambda _, value: value >= min_value
            )
            df = df.withColumn(output_column, tag_map)
            df = df.drop(*tag_columns)
        return df
if __name__ == "__main__":
    app = Silver("/opt/spark/config/silver.yml")
    app.get_table()