class BaseCalculator:

    def __init__(self, valid_operators: list[str]):
        self.__operator = None
        self.__second_number = None
        self.__first_number = None
        self.__valid_operators = valid_operators

    def user_input(self):
        self.__first_number = int(input("Enter first number"))
        self.__second_number = int(input("Enter second number"))
        self.__operator = input("Enter operator")
