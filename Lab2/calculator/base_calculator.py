class BaseCalculator:

    def __init__(self, valid_operators: list[str]):
        self.__operator = None
        self.__second_number = None
        self.__first_number = None
        self.__valid_operators = valid_operators

    def do_operation(self):
        while True:
            self.__user_input()
            result = None
            if self.__operator == '+':
                result = self.__first_number + self.__second_number
            elif self.__operator == '-':
                result = self.__first_number - self.__second_number
            elif self.__operator == '*':
                result = self.__first_number * self.__second_number
            elif self.__operator == '/':
                if self.__second_number == 0:
                    print("Cannot divide by zero\n")
                else:
                    result = self.__first_number / self.__second_number
            print(f"Result: {result}")
            answer = input("Do you wanna create operation again?(y/n)\n")
            if answer.lower() != 'y':
                break

    def __user_input(self):
        self.__first_number = self.__enter_number("Enter first number\n")
        self.__second_number = self.__enter_number("Enter second number\n")
        self.__operator = input("Enter operator\n")

    def __enter_operator(self):
        while True:
            operator = input("Enter operator:\n")
            if operator not in self.__valid_operators:
                print(f"Operator is not valid:{operator}")
            else:
                self.__operator = operator
                break

    @staticmethod
    def __enter_number(input_msg: str = "Enter number:\n") -> float:
        while True:
            user_input = input(input_msg)
            try:
                number = float(user_input)
                return number
            except ValueError:
                print("Invalid number entered.")
