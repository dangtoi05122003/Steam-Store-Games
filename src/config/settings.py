from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    minio_access_key: str = os.getenv("MINIO_ACCESS_KEY")
    minio_secret_key: str = os.getenv("MINIO_ROOT_PASSWORD")
    minio_endpoint: str = os.getenv("MINIO_ENDPOINT")
    bucket_name: str = os.getenv("BUCKET_NAME")
    spark_name: str = os.getenv("SPARK_NAME")
    jar_dir: str = os.getenv("JAR_DIR")
setting = Settings()