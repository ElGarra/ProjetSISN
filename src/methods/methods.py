import numpy as np
import matplotlib.pyplot as plt
from skimage import io, metrics

class ImageComparison:
    def __init__(self, image1_path, image2_path, title):
        self.image1 = io.imread(image1_path)
        self.image2 = io.imread(image2_path)
        self.title = title
        self.ssim = None
        self.mse = None
        self.snr = None
        self.nmi = None

    def calculate_metrics(self):
        # Calculate SSIM
        self.ssim = metrics.structural_similarity(self.image1, self.image2, multichannel=True)
        
        # Calculate MSE
        self.mse = metrics.mean_squared_error(self.image1, self.image2)

        # Calculate SNR
        self.snr = metrics.peak_signal_noise_ratio(self.image1, self.image2)

        # Calculate NMI
        self.nmi = metrics.normalized_mutual_information(self.image1, self.image2)

    def plot_results(self):
        # Create a table to display the metrics
        table_data = [
            ['SSIM', self.ssim],
            ['MSE', self.mse],
            ['SNR', self.snr],
            ['NMI', self.nmi]
        ]
        
        fig, ax = plt.subplots()
        table = ax.table(cellText=table_data, colLabels=['Metric', 'Value'],
                         loc='center', cellLoc='center', bbox=[0, 0, 1, 1])
        table.set_fontsize(14)
        table.scale(1, 1.5)

        # Hide axis
        ax.axis('off')

        # Show the table
        plt.suptitle(f'{self.title}\n')
        plt.show()

    def execute(self):
        self.calculate_metrics()
        self.plot_results()
