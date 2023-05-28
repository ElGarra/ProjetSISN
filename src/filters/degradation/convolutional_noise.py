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

    def add_gaussian_noise(self):
        # Generate the gaussian bruit with the same dimentions of the image
        noise = np.random.normal(self.mean, self.std_dev, self.image_float.shape)
        # Add the bruit to the image
        self.noisy_image = self.image_float + noise
        # Ensures that the values are within the valid range [0, 1]
        self.noisy_image = np.clip(self.noisy_image, 0, 1)
        return self.noisy_image
    
    def add_convolutional_noise(self):
        #convolutional gaussian noise
        output = filters.gaussian(self.image_float, sigma=20) 
        self.noisy_image += output
        return self.noisy_image
        
    def calculate_difference(self):
        # Calculate the diference between the original image and the filtered image
        self.difference = self.image_float - self.noisy_image

    def save_images(self):
        # Save the original image as PNG
        io.imsave(f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/{self.image_name}.png', util.img_as_ubyte(self.image_float))

        # Scale the rebuilt image and the difference to the range [0, 1]
        filtered_image_scaled = util.img_as_float(self.noisy_image)
        difference_scaled = util.img_as_float(self.difference)
        
        # Convert the images to uint8 format
        filtered_image_uint8 = (filtered_image_scaled * 255).astype(np.uint8)
        difference_uint8 = (difference_scaled * 255).astype(np.uint8)
        
        # Save the rebuilt image as PNG
        io.imsave(f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/convolutional_gaussian_filtered_{self.image_name}.png',
                filtered_image_uint8, check_contrast=False)
        
        # Save the difference as PNG
        io.imsave(f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/convolutional_gaussian_difference_{self.image_name}.png',
                difference_uint8, check_contrast=False)
        
    def generate_histogram(self):
        hist, bins = np.histogram(self.difference.flatten(), bins=256, range=(-1, 1))
        # Plot and save the histogram as a PNG image
        plt.figure(figsize=(8, 4))
        plt.plot(bins[:-1], hist, color='black')
        plt.title('Histogram of the difference ( Convolutional + Aditive Noise)')
        plt.xlabel('Pixel value')
        plt.ylabel('Frequency')
        plt.savefig(f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/histogram_degradation_{self.image_name}.png', dpi=300)
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
        axes[1, 0].set_title('Difference (Convolutinal + Aditive Noise)')
        axes[1, 0].axis('off')
        axes[1, 1].hist(self.difference.flatten(), bins=256, color='black')
        axes[1, 1].set_title('Histogram of Difference (Convolutinal + Aditive Noise)')
        axes[1, 1].set_xlabel('Pixel Value')
        axes[1, 1].set_ylabel('Frequency')

        plt.suptitle('Gaussian Noise Adition & Convolution Analysis on Image')
        plt.tight_layout()
        plt.show()


    def execute(self):
        self.charge_image_as_float()
        self.add_gaussian_noise()
        self.add_convolutional_noise()
        self.calculate_difference()
        self.save_images()
        self.generate_histogram()
        self.plot_images()
