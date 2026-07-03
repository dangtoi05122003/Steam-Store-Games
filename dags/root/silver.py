import os
from generators.silver import SilverGenerator

path = os.getenv("AIRFLOW_SILVER_PATH")
generator = SilverGenerator(path = path, layer = 'silver')
generator.load_dags(globals())