import matplotlib.pyplot as plt
import os

class Plotter:
    def __init__(self, image_dir):
        self.image_dir = image_dir
        os.makedirs(self.image_dir, exist_ok=True)

    def plot_and_save(self, combined_df, metric_name):
        plt.figure(figsize=(10, 6))
        for column in combined_df.columns:
            plt.plot(combined_df.index, combined_df[column], marker='o', linestyle='-', label=column)
        plt.title(f'{metric_name}(B) vs. Epoch')
        plt.xlabel('Epoch')
        plt.ylabel(f'{metric_name}')
        plt.grid(True)
        plt.legend()
        plt.show()

        image_path = os.path.join(self.image_dir, f'{metric_name}_vs_Epoch.png'.replace('/', '_'))
        plt.savefig(image_path)
        return image_path
