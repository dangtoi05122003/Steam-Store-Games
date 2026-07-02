from config import setting
from minio import Minio
from utils import get_logger

logger = get_logger(__name__)

class MinioClient:
    def __init__(self):
        self.client = Minio(
            endpoint = setting.minio_endpoint,
            access_key = setting.minio_access_key,
            secret_key = setting.minio_secret_key,
            secure=False
        )
        self.create_bucket(setting.bucket_name)
    def create_bucket(self, bucket_name):
        try:
            if not self.client.bucket_exists(bucket_name):
                self.client.make_bucket(bucket_name)
                logger.info(f"Bucket: {bucket_name} đã được tạo thành công")
        except Exception as e:
            logger.error(f"Lỗi khi tạo bucket: {e}")