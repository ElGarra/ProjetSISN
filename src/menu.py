"""
Script created to work as interactive menu during the execution of the code.
It works in the terminal, please follow the instructions.
"""
import sys
from skimage import data
from .filters.gaussian_noise import GaussianNoise
# from .filters.filters import apply_filter
# from .methods.methods import generate_metrics_table

class Menu():

    def __init__(self) -> None:
        print("####################################################################################################\n")
        print(" --> Welcome to the interactive console of the project 'Methods for improving image quality'\n")
        self.main_question = " --> Which image would you like to work with? Please choose an option:\n\n \
    [1] clock\n \
    [2] moon\n \
    [3] camera\n \
    [4] coins\n \
    [4] hubble_deep_fiel\n \
    [5] Exit\n\n"
        self.error_message = "\nInvalid command, please try again.\n"
        self.main_options_list = list(range(1, 7))
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
            elif option == 4:
                self.image = data.coins()
                self.image_name = "coins"
            elif option == 5:
                self.image = data.hubble_deep_field()
                self.image_name = "hubble_deep_field"
            else:
                sys.exit("See you soon!")
        self.apply_degradation()
        
    def apply_degradation(self):
        gaussian_noise = GaussianNoise(self.image, self.image_name)
        gaussian_noise.execute()

    def execute(self):
        self.options()            


        
