"""
Script created to work as interactive menu during the execution of the code.
It works in the terminal, please follow the instructions.
"""
import sys
from skimage import data, io, filters, util
from .filters.degradation.gaussian_noise import GaussianNoise
from .filters.reconstruction.median_filter import MedianFilter
from .filters.degradation.convolutional_noise import ConvolutionalNoise
from .filters.reconstruction.wiener_filter import WienerFilter
from .methods.methods import ImageComparison
import matplotlib.pyplot as plt
from .methods.analyse import analyse

class Menu():

    def __init__(self):
        print("####################################################################################################\n")
        print(" --> Welcome to the interactive console of the project 'Methods for improving image quality'\n")
        self.main_question = " --> Which image would you like to work with? Please choose an option:\n\n \
    [1] clock\n \
    [2] moon\n \
    [3] camera\n \
    [4] Exit\n\n"
        self.error_message = "\nInvalid command, please try again.\n"
        self.main_options_list = list(range(1, 5))
        self.image_name = ""
        self.filters = ['median', 'gaussian', 'wiener', 'laplace']

    def options(self):
        print("####################################################################################################\n")
        option = int(input(self.main_question))
        if not option in self.main_options_list:
            print(self.error_message)
            option = int(input(self.main_question))
        else:
            if option == 1:
                self.image = data.clock()
                self.image_name = "clock"
            elif option == 2:
                self.image = data.moon()
                self.image_name = "moon"
            elif option == 3:
                self.image = data.camera()
                self.image_name = "camera"
            else:
                sys.exit("See you soon!")
        
    def apply_filters(self):
        self.gaussian_noise = GaussianNoise(self.image, self.image_name)
        self.gaussian_noise.execute()
        self.median_filter = MedianFilter(self.gaussian_noise.image_name)
        self.median_filter.execute()
        self.convolutional_noise = ConvolutionalNoise(self.image, self.image_name)
        self.convolutional_noise.execute()
        self.wiener_filter = WienerFilter(self.convolutional_noise.image_name)
        self.wiener_filter.execute()

    def show_summary(self):
        # Load the first set of images
        noisy_image1 = io.imread(f'assets/aditiveGaussianDegradationMedianReconstruction/{self.image_name}/aditive_gaussian_filtered_{self.image_name}.png')
        rebuilt_image1 = io.imread(f'assets/aditiveGaussianDegradationMedianReconstruction/{self.image_name}/median_rebuilt_{self.image_name}.png')

        # Load the second set of images
        noisy_image2 = io.imread(f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/convolutional_gaussian_filtered_{self.image_name}.png')
        rebuilt_image2 = io.imread(f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/wiener_rebuilt_{self.image_name}.png')

        # Configure the size of the figure and subplots
        fig, axes = plt.subplots(2, 3, figsize=(12, 8))

        # Set the main titles for each set of images
        main_title1 = 'Analysis of degradation with additive Gaussian noise & median-filtered reconstruction'
        main_title2 = 'Analysis of degradation with additive + Convolutional Gaussian noise & wiener-filtered reconstruction'

        # Set the main titles for each set of images
        fig.suptitle(main_title1, fontsize=16)

        # Set titles for the first set of images
        axes[0, 0].set_title('Original Image')
        axes[0, 1].set_title('Degraded Image')
        axes[0, 2].set_title('Filtered Image')

        # Show the first set of images
        axes[0, 0].imshow(self.image, cmap='gray')
        axes[0, 1].imshow(noisy_image1, cmap='gray')
        axes[0, 2].imshow(rebuilt_image1, cmap='gray')

        # Hide the axis labels for the first row
        axes[0, 0].axis('off')
        axes[0, 1].axis('off')
        axes[0, 2].axis('off')

        # Update the main title for the second set of images
        fig.suptitle(main_title2, fontsize=16)

        # Set titles for the second set of images
        axes[1, 0].set_title('Original Image')
        axes[1, 1].set_title('Degraded Image')
        axes[1, 2].set_title('Filtered Image')

        # Show the second set of images
        axes[1, 0].imshow(self.image, cmap='gray')
        axes[1, 1].imshow(noisy_image2, cmap='gray')
        axes[1, 2].imshow(rebuilt_image2, cmap='gray')

        # Hide the axis labels for the second row
        axes[1, 0].axis('off')
        axes[1, 1].axis('off')
        axes[1, 2].axis('off')

        # Adjust the space between subplots and show the figure
        plt.tight_layout()
        plt.show()

    def calculate_methods(self):
        methods = [
            {
                'method': 'Aditive/Median',
                'degraded_path': f'assets/aditiveGaussianDegradationMedianReconstruction/{self.image_name}/aditive_gaussian_filtered_{self.image_name}.png',
                'rebuilt_path': f'assets/aditiveGaussianDegradationMedianReconstruction/{self.image_name}/median_rebuilt_{self.image_name}.png',
                'title_1': "Measures Original image vs Degraded image in Aditive noise/Median",
                'title_2': "Measures Original image vs Rebuilt image in Aditive noise/Median"
            },
            {
                'method': 'Convolution & Adition/Wiener',
                'degraded_path': f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/convolutional_gaussian_filtered_{self.image_name}.png',
                'rebuilt_path': f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/wiener_rebuilt_{self.image_name}.png',
                'title_1': "Measures Original image vs Degraded image in Convolution/Wiener",
                'title_2': "Measures Original image vs Rebuilt image in Convolution/Wiener"
            }
        ]

        for method in methods:
            original_path = f'assets/aditiveGaussianDegradationMedianReconstruction/{self.image_name}/{self.image_name}.png'
            degraded_path = method['degraded_path']
            rebuilt_path = method['rebuilt_path']
            title_1 = method['title_1']
            title_2 = method['title_2']

            comparison_1 = ImageComparison(original_path, degraded_path, rebuilt_path, title_1)
            comparison_1.execute()
            #comparison_2 = ImageComparison(original_path, rebuilt_path, title_2)
            #comparison_2.execute()

    def analysis(self):
        #set second argument to 1 for normalized data
        ana = analyse(self.image, 0, 1)
        ana.execute()

    def execute(self):
        self.options() 
        self.apply_filters()   
        self.show_summary()
        self.analysis()       
        self.calculate_methods()