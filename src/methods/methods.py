import numpy as np
import matplotlib.pyplot as plt
from skimage import io, metrics

class ImageComparison:
    def __init__(self, image1_path, image2_path, image3_path, title):
        self.images = [None] * 2
        self.image1 = io.imread(image1_path)
        self.images[0] = io.imread(image2_path)
        self.images[1] = io.imread(image3_path)
        self.title = title
        self.ssim =[None] * 2
        self.mse = [None] * 2
        self.snr = [None] * 2
        self.nmi = [None] * 2

    def calculate_metrics(self):
        for i in range(len(self.images)):
            # Calculate SSIM
            self.ssim[i] = metrics.structural_similarity(self.image1, self.images[i], multichannel=True)
            
            # Calculate MSE
            self.mse[i] = metrics.mean_squared_error(self.image1, self.images[i])

            # Calculate SNR
            self.snr[i] = metrics.peak_signal_noise_ratio(self.image1, self.images[i])

            # Calculate NMI
            self.nmi[i] = metrics.normalized_mutual_information(self.image1, self.images[i])

    def plot_results(self):
        # Create a table to display the metrics
        table_data = [
            ['Image', 'SSIM', 'MSE', 'SNR', 'NMI'],
            ['Degraded Image', self.ssim[0], self.mse[0], self.snr[0], self.nmi[0]],
            ['Rebuilt Image', self.ssim[1], self.mse[1], self.snr[1], self.nmi[1]],
        ]
        
        fig, ax = plt.subplots()
        table = ax.table(cellText=table_data,
                         loc='center', cellLoc='center')
        table.set_fontsize(100)
        table.scale(1.25, 1.5)

        # Hide axis
        ax.axis('off')

        # Show the table
        plt.suptitle(f'{self.title}\n')
        plt.show()

    def execute(self):
        self.calculate_metrics()
        self.plot_results()
