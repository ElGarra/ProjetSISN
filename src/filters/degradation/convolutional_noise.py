import numpy as np
import matplotlib.pyplot as plt
from skimage import data, util, io, filters

class ConvolutionalNoise():
    def __init__(self, image, image_name):
        self.image = image
        self.image_name = image_name
        self.image_float = None
        self.noisy_image = None
        self.difference = None
        self.mean = 0
        self.std_dev = 0.15

    def charge_image_as_float(self):
        # Convert the image to float oint within the valid range [0, 1]
        self.image_float = util.img_as_float(self.image)

    def add_convolutional_noise(self):
        #additive gaussian noise
        noise = np.ones_like(self.image_float) * 0.2 * (self.imgage_float.max() - self.imgae_float.min())
        rng = np.random.default_rng()
        noise[rng.random(size=noise.shape) > 0.5] *= -1

        #convolutional gaussian noise
        output = filters.gaussian(self.image_float, sigma=self.std_dev) 
        self.noisy_image = output + noise
        return self.noisy_image
        
    def calculate_difference(self):
        # Calculate the diference between the original image and the filtered image
        self.difference = self.image_float - self.noisy_image

    def save_images(self):
        # Save the original image as PNG
        io.imsave(f'assets/aditiveGaussianDegradationMedianReconstruction/{self.image_name}/{self.image_name}.png', util.img_as_ubyte(self.image_float))
        # Save the filtered image as PNG
        io.imsave(f'assets/aditiveGaussianDegradationMedianReconstruction/{self.image_name}/aditive_gaussian_filtered_{self.image_name}.png', util.img_as_ubyte(self.noisy_image))
        # Save the difference as PNG
        io.imsave(f'assets/aditiveGaussianDegradationMedianReconstruction/{self.image_name}/aditive_gaussian_difference_{self.image_name}.png', util.img_as_ubyte(self.difference))

    def generate_histogram(self):
        hist, bins = np.histogram(self.difference.flatten(), bins=256, range=(-1, 1))
        # Plot and save the histogram as a PNG image
        plt.figure(figsize=(8, 4))
        plt.plot(bins[:-1], hist, color='black')
        plt.title('Histogram of the difference (Noise)')
        plt.xlabel('Pixel value')
        plt.ylabel('Frequency')
        plt.savefig(f'assets/aditiveGaussianDegradationMedianReconstruction/{self.image_name}/histogram_degradation_{self.image_name}.png', dpi=300)
        plt.close()

    def plot_images(self):
        fig, axes = plt.subplots(2, 2, figsize=(8, 8))
        axes[0, 0].imshow(self.image_float, cmap='gray')
        axes[0, 0].set_title('Original Image')
        axes[0, 0].axis('off')
        axes[0, 1].imshow(self.noisy_image, cmap='gray')
        axes[0, 1].set_title('Noisy Image')
        axes[0, 1].axis('off')
        axes[1, 0].imshow(self.difference, cmap='gray')
        axes[1, 0].set_title('Difference (Noise)')
        axes[1, 0].axis('off')
        axes[1, 1].hist(self.difference.flatten(), bins=256, color='black')
        axes[1, 1].set_title('Histogram of Difference (Noise)')
        axes[1, 1].set_xlabel('Pixel Value')
        axes[1, 1].set_ylabel('Frequency')

        plt.suptitle('Gaussian Noise Adition Analysis on Image')
        plt.tight_layout()
        plt.show()


    def execute(self):
        self.charge_image_as_float()
        self.add_gaussian_noise()
        self.calculate_difference()
        self.save_images()
        self.generate_histogram()
        self.plot_images()
