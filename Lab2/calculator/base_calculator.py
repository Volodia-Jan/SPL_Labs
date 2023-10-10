class BaseCalculator:

    def __init__(self, valid_operators: list[str]):
        self._operator = None
        self._second_number = None
        self._first_number = None
        self.__valid_operators = valid_operators

    def do_operation(self):
        while True:
            result = self.perform_operation()
            if result is not None:
                print(f"Result: {result}")
            answer = input("Do you want to perform another operation?(y/n)\n")
            if answer.lower() != 'y':
                break

    def perform_operation(self):
        self.__user_input()
        result = None
        if self._operator == '+':
            result = self._first_number + self._second_number
        elif self._operator == '-':
            result = self._first_number - self._second_number
        elif self._operator == '*':
            result = self._first_number * self._second_number
        elif self._operator == '/':
            if self._second_number == 0:
                print("Cannot divide by zero\n")
            else:
                result = self._first_number / self._second_number
        return result

    def __user_input(self):
        self._first_number = self.__enter_number("Enter first number\n")
        self._second_number = self.__enter_number("Enter second number\n")
        self._operator = input("Enter operator\n")

    def __enter_operator(self):
        while True:
            operator = input("Enter operator:\n")
            if operator not in self.__valid_operators:
                print(f"Operator is not valid:{operator}")
            else:
                self._operator = operator
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
