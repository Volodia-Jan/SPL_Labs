import math

from calculator.calculation_settings import CalculationSettings
from calculator.calculator_memory import CalculationMemory


class Calculator:

    def __init__(self, file_name: str):
        self.__memory = CalculationMemory(file_name)

    def setup_calculator(self, valid_operators: list[str]):
        self.__pick_init_type(valid_operators)

    def do_operation(self) -> float:
        result = None
        if self.__operator == '+':
            result = self.__first_number + self.__second_number
        elif self.__operator == '-':
            result = self.__first_number - self.__second_number
        elif self.__operator == '*':
            result = self.__first_number * self.__second_number
        elif self.__operator == '/':
            if self.__second_number == 0:
                print("Cannot divide by zero")
            else:
                result = self.__first_number / self.__second_number
        elif self.__operator == '^':
            result = pow(self.__first_number, self.__second_number)
        elif self.__operator == '%':
            result = self.__first_number % self.__second_number
        elif self.__operator == 'sqrt':
            result = self.__get_sqrt()
        else:
            print("Invalid operator passed")
        self.__save_option(result)

        return result

    def print_history(self):
        print(self.__memory.get_formatted_string_data())

    def clear_memory(self):
        print(self.__memory.clear_memory())

    def __pick_init_type(self, valid_operators: list[str]):
        flag = True
        option = int(input("Choose option:\n1 - Create new operation\n2 - use numbers from memory\n"))
        while flag:
            if option == 1:
                self.__new_init(valid_operators)
                flag = False
            elif option == 2:
                self.__init_from_memory(valid_operators)
                flag = False
            else:
                print("Invalid option entered")

    def __save_option(self, result):
        option = input("Do you wanna save data into file?(y/n)")
        if option == 'y':
            self.__memory.add_record(self.__first_number, self.__second_number, self.__operator, result)
        else:
            print("Ok, let's move on")

    def __new_init(self, valid_operators):
        self.__first_number = Calculator.__enter_number("Enter first number\n")
        self.__second_number = Calculator.__enter_number("Enter second number\n")
        self.__operator = Calculator.__enter_operator(valid_operators,
                                                      f"Enter operator:\nValid operators:{valid_operators}\n")

    def __init_from_memory(self, valid_operators: list[str]):
        print("Choose memory data from list by its index:")
        self.print_history()
        index = int(input('Enter index:\n'))
        record = self.__memory.get_record_by_index(index)
        if record is None:
            print('Invalid index')
            return

        self.__first_number = record["firstNumber"]
        self.__second_number = record["secondNumber"]
        self.__operator = self.__enter_operator(valid_operators, "Enter new operator:\n")

    def __get_sqrt(self) -> float:
        print(f"Your numbers:\n1 - {self.__first_number}\n2 - {self.__second_number}")
        option = int(input("Choose the number that should be converted?\n"))
        if option == 1:
            if self.__first_number < 0:
                print(f"Cannot get square of {self.__first_number} cause it is < 0")
            else:
                return math.sqrt(self.__first_number)
        if option == 2:
            if self.__second_number < 0:
                print(f"Cannot get square of {self.__second_number} cause it is < 0")
            else:
                return math.sqrt(self.__second_number)

    @staticmethod
    def __enter_operator(valid_operators: list[str], input_message: str = "Enter operator\n") -> str:
        while True:
            operator = input(input_message)
            if operator in valid_operators:
                return operator
            else:
                print("Invalid operator entered.")
                print(f"Valid operators: {valid_operators}")

    @staticmethod
    def __enter_number(input_msg: str = "Enter number:\n") -> float:
        while True:
            user_input = input(input_msg)
            try:
                number = float(user_input)
                return number
            except ValueError:
                print("Invalid number entered.")
