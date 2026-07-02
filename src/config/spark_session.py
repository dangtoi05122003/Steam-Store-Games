from pyspark.sql import SparkSession
from config import setting
from utils.spark_jars import load_jars
jars = load_jars()
def get_spark(jars = jars):
    return SparkSession.builder \
        .appName(setting.spark_name) \
        .config("spark.jars", jars) \
        .master("spark://spark-master:7077") \
        .config("spark.hadoop.fs.s3a.endpoint", f"http://{setting.minio_endpoint}") \
        .config("spark.hadoop.fs.s3a.access.key", setting.minio_access_key) \
        .config("spark.hadoop.fs.s3a.secret.key", setting.minio_secret_key) \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
        .getOrCreate()