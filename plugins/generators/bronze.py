from generators.DagGenerator import Generators

class BronzeGenerator(Generators):
    def __init__(self, path, layer):
        super().__init__(path, layer)
    def get_bash_command(self, task):
        return f"docker exec spark-master /opt/spark/bin/spark-submit --jars /opt/spark/extra_jars/hadoop-aws-3.3.4.jar,/opt/spark/extra_jars/aws-java-sdk-bundle-1.12.262.jar {task['script_path']}"