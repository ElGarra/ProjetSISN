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
        # self.gaussian_noise = GaussianNoise(self.image, self.image_name)
        # self.gaussian_noise.execute()
        # self.median_filter = MedianFilter(self.gaussian_noise.image_name)
        # self.median_filter.execute()
        self.convolutional_noise = ConvolutionalNoise(self.image, self.image_name)
        self.convolutional_noise.execute()
        self.wiener_filter = WienerFilter(self.convolutional_noise.image_name)
        self.wiener_filter.execute()

    def show_summary(self):
        # self.noisy_image = io.imread(f'assets/aditiveGaussianDegradationMedianReconstruction/{self.image_name}/aditive_gaussian_filtered_{self.image_name}.png')
        self.noisy_image = io.imread(f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/convolutional_gaussian_filtered_{self.image_name}.png')
        # self.rebuilt_image = io.imread(f'assets/aditiveGaussianDegradationMedianReconstruction/{self.image_name}/median_rebuilt_{self.image_name}.png')
        self.rebuilt_image = io.imread(f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/wiener_rebuilt_{self.image_name}.png')
        # Configurar el tamaño de la figura y los subplots
        fig, axes = plt.subplots(1, 3, figsize=(12, 4))

        # Mostrar la imagen original
        axes[0].imshow(self.image, cmap='gray')
        axes[0].set_title('Original Image')
        axes[0].axis('off')

        # Mostrar la imagen degradada con ruido
        axes[1].imshow(self.noisy_image, cmap='gray')
        axes[1].set_title('degraded Image')
        axes[1].axis('off')

        # Mostrar la imagen reconstruida con filtro de mediana
        axes[2].imshow(self.rebuilt_image, cmap='gray')
        axes[2].set_title('Filtered Image')
        axes[2].axis('off')

        # Agregar leyendas en inglés
        axes[0].set_title('Original Image')
        axes[1].set_title('degraded Image')
        axes[2].set_title('rebuilt Image')

        # Ajustar el espacio entre subplots y mostrar la figura
        # plt.suptitle('Analysis of degradation with additive Gaussian noise & median-filtered reconstruction\n')
        plt.suptitle('Analysis of degradation with additive + Convolutional Gaussian noise & wiener-filtered reconstruction\n')
        plt.tight_layout()
        plt.show()

    def calculate_methods(self):
        self.original_path = f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/{self.image_name}.png'
        self.degradated_path = f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/convolutional_gaussian_filtered_{self.image_name}.png'
        self.rebuilt_path = f'assets/aditiveConvolutionalGaussianDegradationWienerReconstruction/{self.image_name}/wiener_rebuilt_{self.image_name}.png'
        self.comparison_1 = ImageComparison(self.original_path, self.degradated_path)
        self.comparison_1.execute()
        self.comparison_2 = ImageComparison(self.original_path, self.rebuilt_path)
        self.comparison_2.execute()


    def execute(self):
        self.options()  
        self.apply_filters()   
        self.show_summary()       
        self.calculate_methods()



        
