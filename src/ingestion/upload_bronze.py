from config import MinioClient
from config.spark_session import get_spark
from utils import load_yaml, get_logger
import os
from config import setting
logger = get_logger(__name__)

class UploadBronze:
    def __init__(self, path):
        MinioClient()
        self.config = load_yaml(path)
        self.spark = get_spark()
    def ingest_csv_to_bronze(self):
        data_path = self.config["path"]
        for file in os.listdir(data_path):
            if file.endswith(".csv"):
                full_path = os.path.join(data_path, file)
                logger.info(f"Đang đọc file: {full_path}")
                df = self.spark.read.option("header", True).option("multiLine", True).option("quote", "\"").option("escape", "\"").csv(full_path)
                table_name = file.replace(".csv", "")
                output_path = f"s3a://{setting.bucket_name}/bronze/{table_name}/"
                df.write.mode("overwrite").parquet(output_path)
                logger.info(f"Đã upload lên MinIO: {output_path}")
if __name__ == '__main__':
    app = UploadBronze("/opt/spark/config/bronze.yml")
    app.ingest_csv_to_bronze()