from config import TrinoConfig, setting
from utils import load_yaml

class Schema:
    def __init__(self, path):
        self.config = load_yaml(path)
        self.cursor = TrinoConfig()
    def create_all_tables(self):
        for table_name, table_config in self.config['tables'].items():
            self.cursor.create_table(table_name, table_config['columns'], self.config['path']['source'].format(bucket_name = setting.bucket_name))

if __name__ == "__main__":
    app = Schema("/opt/airflow/config/schema.yml")
    app.create_all_tables()