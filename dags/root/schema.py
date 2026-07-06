import os
from generators.schema import SchemaGenerator

path = os.getenv("AIRFLOW_SCHEMA_PATH")
generator = SchemaGenerator(path = path, layer = 'schema')
generator.load_dags(globals())