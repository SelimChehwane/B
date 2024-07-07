import os
import yaml
#Imports modules

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')#Constructs the path
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)#Opens the file in read mode

config = load_config()
print(config['variable2'])#Accesses variable from the file