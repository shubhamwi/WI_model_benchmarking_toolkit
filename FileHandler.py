import os
import yaml

class FileHandler:
    def __init__(self, csv_directory, config_file):
        self.csv_directory = csv_directory
        self.config_file = config_file

    def list_csv_files(self):
        return [f for f in os.listdir(self.csv_directory) if f.endswith('.csv')]

    def read_yaml_config(self):
        with open(self.config_file, 'r') as yaml_file:
            return yaml.safe_load(yaml_file)
