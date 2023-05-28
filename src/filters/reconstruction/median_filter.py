import numpy as np
import matplotlib.pyplot as plt
from skimage import filters, util, io, morphology

class MedianFilter():
    def __init__(self, image_name):
        self.image_name = image_name
        self.image = None
        self.rebuilt_image = None
        self.difference = None
        self.footprint = morphology.square(5)

    def load_image(self):
        self.image = io.imread(f'assets/aditiveGaussianDegradationMedianReconstruction/{self.image_name}/aditive_gaussian_filtered_{self.image_name}.png')

    def apply_median_filter(self):
        self.rebuilt_image = filters.median(self.image, footprint=None, out=None, mode='nearest', cval=0.0, behavior='ndimage')

    def calculate_difference(self):
        self.difference = self.image - self.rebuilt_image

    def save_images(self):
       # Save the reconstrucred image as PNG
        io.imsave(f'assets/aditiveGaussianDegradationMedianReconstruction/{self.image_name}/median_rebuilt_{self.image_name}.png', util.img_as_ubyte(self.rebuilt_image))
        # Save the difference as PNG
        io.imsave(f'assets/aditiveGaussianDegradationMedianReconstruction/{self.image_name}/median_filtered_difference_{self.image_name}.png', util.img_as_ubyte(self.difference))


    def plot_results(self):
        fig, axes = plt.subplots(1, 3, figsize=(12, 3))
        axes[0].imshow(self.image, cmap='gray')
        axes[0].set_title('Degradated Image')
        axes[0].axis('off')
        axes[1].imshow(self.rebuilt_image, cmap='gray')
        axes[1].set_title('Rebuilt Image')
        axes[1].axis('off')
        axes[2].imshow(self.difference, cmap='gray')
        axes[2].set_title('Difference')
        axes[2].axis('off')
        plt.suptitle('Median Filter Analysis')
        plt.tight_layout()
        plt.show()


    def execute(self):
        self.load_image()
        self.apply_median_filter()
        self.calculate_difference()
        # self.generate_histogram()
        self.save_images()
        self.plot_results()
