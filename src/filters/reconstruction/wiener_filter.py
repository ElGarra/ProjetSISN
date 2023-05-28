import numpy as np
import matplotlib.pyplot as plt
from skimage import filters, util, io

class WienerFilter():
    def __init__(self, image_name):
        self.image_name = image_name
        self.image = None
        self.rebuilt_image = None
        self.difference = None
        self.std_dev = 20

    def load_image(self):
        self.image = io.imread(f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/convolutional_gaussian_filtered_{self.image_name}.png')
        self.image_float = util.img_as_float(self.image)

    def gaussian_impulse_response(self):
        x = np.linspace(-self.impulse_response_size // 2, self.impulse_response_size // 2, self.impulse_response_size)
        y = np.exp(-(x ** 2) / (2 * self.std_dev ** 2))
        return y / np.sum(y)
    
    def gaus_callable(self, *arg, **kwargs):
        return self.impulse_response
    
    def apply_wiener_filter(self):
        # Define Gaussian impulse response parameters
        self.impulse_response_size = (self.image.shape[0] + 1) * (self.image.shape[1] + 1)
        #self.image_float.shape

        # Generate the Gaussian impulse response
        self.impulse_response = self.gaussian_impulse_response()
            
        # Apply Wiener filtering with the impulse response
        self.rebuilt_image = filters.wiener(self.image_float, self.gaus_callable)
    
        return self.rebuilt_image

    def calculate_difference(self):
        self.difference = self.image - self.rebuilt_image

    # def save_images(self):
    #    # Save the reconstrucred image as PNG
    #     io.imsave(f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/wiener_rebuilt_{self.image_name}.png', util.img_as_ubyte(self.rebuilt_image))
    #     print("Primera")
    #     # Save the difference as PNG
    #     io.imsave(f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/wiener_filtered_difference_{self.image_name}.png', util.img_as_ubyte(self.difference))
    #     print("Segunda")

    def save_images(self):
        # Scale the rebuilt image and the difference to the range [0, 1]
        rebuilt_image_scaled = util.img_as_float(self.rebuilt_image)
        difference_scaled = util.img_as_float(self.difference)
        
        # Convert the images to uint8 format
        rebuilt_image_uint8 = (rebuilt_image_scaled * 255).astype(np.uint8)
        difference_uint8 = (difference_scaled * 255).astype(np.uint8)
        
        # Save the rebuilt image as PNG
        io.imsave(f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/wiener_rebuilt_{self.image_name}.png',
                rebuilt_image_uint8, check_contrast=False)
        
        # Save the difference as PNG
        io.imsave(f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/wiener_filtered_difference_{self.image_name}.png',
                difference_uint8, check_contrast=False)


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
        plt.suptitle('Wiener Filter Analysis')
        plt.tight_layout()
        plt.show()


    def execute(self):
        self.load_image()
        self.apply_wiener_filter()
        self.calculate_difference()
        # self.generate_histogram()
        self.save_images()
        self.plot_results()
