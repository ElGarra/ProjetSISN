"""
Script created to work as interactive menu during the execution of the code.
It works in the terminal, please follow the instructions.
"""
import sys

class Menu():

    def __init__(self) -> None:
        print("####################################################################################################\n")
        print(" --> Welcome to the interactive console of the project 'Methods for improving image quality'\n")
        self.main_question = " --> What would you like to do now? Please choose an option:\n\n \
    [1] Apply all filters in all images\n \
    [2] Apply all filters in one image\n \
    [3] Apply one filter in all images\n \
    [4] Apply one filter in one image\n \
    [5] Exit\n\n"
        self.error_message = "\nInvalid command, please try again.\n"
        self.main_options_list = list(range(1, 6))

    def options(self):
        print("####################################################################################################\n")
        option = int(input(self.main_question))
        if not option in self.main_options_list:
            print(self.error_message)
            option = int(input(self.main_question))
        else:
            if option == 1:
                # Call respective function for 1
                print(option)
            elif option == 2:
                # Call respective function for 2
                print(option)
            elif option == 3:
                # Call respective function for 3
                print(option)
            elif option == 4:
                # Call respective function for 4
                print(option)
            else:
                sys.exit("See you soon!")

    def execute(self):
        self.options()            


        
