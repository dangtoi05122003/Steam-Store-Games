from trino.dbapi import connect
from config import setting
from utils import get_logger

logger = get_logger(__name__)

class TrinoConfig:
    def __init__(self):
        self.cursor = self.connect_trino()
    def connect_trino(self):
        conn = connect(
            host = setting.trino_endpoint,
            port = setting.trino_port,
            user = setting.trino_user,
            catalog = setting.trino_catalog,
            schema =  setting.trino_schema
        )
        logger.info("Đã kết nối đến Trino")
        return conn.cursor()
    def create_table(self, tablename, columns, path):
        logger.info(f"Đang tạo bảng: {tablename}")
        try:
            column = ',\n'.join([f"{col} {dtype}" for col, dtype in columns.items()])
            self.drop_table(tablename)
            self.cursor.execute(f"""
                CREATE TABLE {setting.trino_catalog}.{setting.trino_schema}.{tablename}({column})
                with(
                    external_location = '{path}/{tablename}',
                    format = 'PARQUET'
                )    
            """)
        except Exception:
            logger.exception(f"Lỗi tạo bảng {tablename}")
            raise
    def drop_table(self, tablename):
        logger.info(f"Đang xóa bảng: {tablename}")
        try:
            self.cursor.execute(
                f"DROP TABLE IF EXISTS {setting.trino_catalog}.{setting.trino_schema}.{tablename}"
            )
        except Exception:
            logger.exception(f"Lỗi xóa bảng: {tablename}")
            raise