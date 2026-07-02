from config.settings import setting
import os

def load_jars():
    return ",".join([
        os.path.join(setting.jar_dir, f)
        for f in os.listdir(setting.jar_dir)
        if f.endswith(".jar")
    ])