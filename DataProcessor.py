import pandas as pd
import os

class DataProcessor:
    def __init__(self, csv_directory, config):
        self.csv_directory = csv_directory
        self.config = config

    def process_data(self):
        combined_df = pd.DataFrame()
        csv_files = [f for f in os.listdir(self.csv_directory) if f.endswith('.csv')]
        for csv_file in csv_files:
            df = pd.read_csv(os.path.join(self.csv_directory, csv_file))
            df.columns = df.columns.str.strip()
            base_name, _ = os.path.splitext(csv_file)
            metric_name = self.config[base_name]
            combined_df[base_name] = df[metric_name]
        return combined_df, metric_name
