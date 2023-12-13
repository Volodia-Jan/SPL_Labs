# Represents input helper functionality
import logging


class UserInputHelper:
    # Gets user input
    @staticmethod
    def get_user_input(input_message: str) -> str:
        logging.info('Getting user input')
        return input(input_message)

    # Gets only integer user input
    @staticmethod
    def get_int_user_input(input_message: str) -> int:
        logging.info('Getting user number input')
        while True:
            x = input(input_message)
            try:
                number = int(x)
                return number
            except ValueError:
                print(f"Значення має бути цілим числом. Ваше значення: {x}")

    # Gets only input that contains provided list
    @staticmethod
    def get_limited_user_input(input_message: str, limit: list[str]) -> str:
        logging.info(f'Get user input from range: {limit}')
        while True:
            x = input(input_message)
            if x in limit:
                return x
            else:
                print(f"Ваше значення має бути одним з {limit}")
