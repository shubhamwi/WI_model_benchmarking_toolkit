from FileHandler import FileHandler
from DataProcessor import DataProcessor
from Plotter import Plotter

# Directory and file configurations
csv_directory = 'predictions/'
config_file = 'config_files/config.yaml'
image_dir = './images/'

# Create instances of classes
file_handler = FileHandler(csv_directory, config_file)
data_processor = DataProcessor(csv_directory, file_handler.read_yaml_config())
plotter = Plotter(image_dir)

# Process and plot data
combined_df, metric_name = data_processor.process_data()
image_path = plotter.plot_and_save(combined_df, metric_name)
print(f"Image saved to: {image_path}")
