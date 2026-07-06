from generators.DagGenerator import Generators

class GoldGenerator(Generators):
    def __init__(self, path, layer):
        super().__init__(path, layer)
    def get_bash_command(self, task):
        return f"cd {task['script_path']} && dbt run --profiles-dir /opt/airflow"