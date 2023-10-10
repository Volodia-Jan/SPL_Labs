class BaseCalculator:

    def __init__(self, valid_operators: list[str]):
        self.__operator = None
        self.__second_number = None
        self.__first_number = None
        self.__valid_operators = valid_operators

    def do_operation(self):
        if self.__operator == '+':
            return self.__first_number + self.__second_number
        elif self.__operator == '-':
            return self.__first_number - self.__second_number
        elif self.__operator == '*':
            return self.__first_number * self.__second_number
        elif self.__operator == '/':
            return self.__first_number / self.__second_number

    def user_input(self):
        self.__first_number = int(input("Enter first number"))
        self.__second_number = int(input("Enter second number"))
        self.__operator = input("Enter operator")

    def __enter_operator(self):
        while True:
            operator = input("Enter operator:")
            if operator not in self.__valid_operators:
                print(f"Operator is not valid:{operator}")
            else:
                self.__operator = operator
                break
