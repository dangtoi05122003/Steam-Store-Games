import os
from generators.bronze import BronzeGenerator

path = os.getenv("AIRFLOW_BRONZE_PATH")
generator = BronzeGenerator(path = path, layer = 'bronze')
generator.load_dags(globals())