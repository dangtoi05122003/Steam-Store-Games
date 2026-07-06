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
    trino_endpoint: str = os.getenv("TRINO_ENDPOINT")
    trino_port: int = os.getenv("TRINO_PORT")
    trino_user: str = os.getenv("TRINO_USER")
    trino_catalog: str = os.getenv("TRINO_CATALOG")
    trino_schema : str = os.getenv("TRINO_SCHEMA")
setting = Settings()