import os
from generators.gold import GoldGenerator

path = os.getenv("AIRFLOW_GOLD_PATH")
generator = GoldGenerator(path = path, layer = 'dbt')
generator.load_dags(globals())