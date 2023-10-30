class UserInputHelper:

    @staticmethod
    def get_user_input(input_message: str) -> str:
        return input(input_message)

    @staticmethod
    def get_int_user_input(input_message: str) -> int:
        while True:
            x = input(input_message)
            try:
                number = int(x)
                return number
            except ValueError:
                print(f"Value must be integer. Your value: {x}")

    @staticmethod
    def get_limited_user_input(input_message: str, limit: list[str]) -> str:
        while True:
            x = input(input_message)
            if x in limit:
                return x
            else:
                print(f"Your value must be one of {limit}")
