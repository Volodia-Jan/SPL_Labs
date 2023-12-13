import logging

from Lab1 import execute_lab1
from Lab2 import execute_lab2
from Lab3 import execute_lab3
from Lab4 import execute_lab4
from Lab5 import execute_lab5
from Lab6 import execute_lab6
from Lab7 import execute_lab7
from Lab8 import execute_lab8
from utils import UserInputHelper


# Class runner that can execute every lab work
class LabRunner:

    # Lab runner constructor
    def __init__(self):
        self.labs = {
            "1": execute_lab1,
            "2": execute_lab2,
            "3": execute_lab3,
            "4": execute_lab4,
            "5": execute_lab5,
            "6": execute_lab6,
            "7": execute_lab7,
            "8": execute_lab8,
        }

    # Executing specific lab work
    def __run_lab(self, lab_number):
        try:
            self.labs[lab_number]()
        except KeyError:
            print(f"Lab {lab_number} is not available.")

    # Show all available labs
    def list_labs(self):
        logging.info("Showing list of all labs")
        for lab in self.labs.keys():
            print(f"Lab {lab}")

    # Executing runner
    def run(self):
        logging.info("Executing labs runner")
        while True:
            self.list_labs()
            lab_number = UserInputHelper.get_limited_user_input("Enter number of lab(1-8) or 0 to exit",
                                                                ['1', '2', '3', '4', '5', '6', '7', '8', '0'])
            if lab_number.lower() == '0':
                break
            self.__run_lab(lab_number)


if __name__ == "__main__":
    LabRunner().run()
