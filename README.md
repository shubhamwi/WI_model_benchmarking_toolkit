
# Machine Learning Model Benchmarking Toolkit

## Overview
This toolkit is designed to benchmark various types of machine learning models, including classification, detection, and segmentation models. It processes prediction results stored in CSV files, combines them, and generates a visual representation of the performance metrics over epochs.

## Structure
The toolkit is divided into the following modules:

1. **FileHandler.py**: Manages file operations such as reading CSV files and YAML configurations.
2. **DataProcessor.py**: Processes the CSV data, combining and cleaning it as necessary.
3. **Plotter.py**: Generates plots from the processed data.
4. **main.py**: The main script that orchestrates the use of the above modules.

## Usage
1. **Setup**: 
   - Ensure that all prediction results are stored in CSV files within a single directory.
   - Configure the `config.yaml` file to map CSV filenames to specific metrics.
2. **Execution**:
   - Run `main.py` to process the CSV files and generate plots.
   - The plots will illustrate the performance of different models over epochs.

## Requirements
- Python 3
- Pandas
- Matplotlib
- PyYAML

## Customization
- Modify the `config.yaml` file to suit the specific metrics and models you are benchmarking.
- Adjust the plotting parameters in `Plotter.py` for different visual styles or data presentations.

## Note
This toolkit is flexible and can be adapted to various types of machine learning model benchmarking. Ensure that the CSV files are formatted correctly and the YAML configuration matches the CSV filenames and desired metrics.
