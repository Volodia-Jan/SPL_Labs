import json


class CalculationMemory:

    def __init__(self, file_name):
        self.__file_name = file_name
        self.__data = self.__load_data()

    def add_record(self, first_number, second_number, operator, result):
        index = len(self.__data)
        record = {
            "index": index,
            "firstNumber": first_number,
            "secondNumber": second_number,
            "operator": operator,
            "result": result
        }
        self.__data.append(record)
        self.__save_data()

    def get_all_records(self):
        return self.__data

    def clear_memory(self):
        self.__data = []
        self.__save_data()

    def get_record_by_index(self, index):
        for record in self.__data:
            if record["index"] == index:
                return record
        return None

    def get_formatted_string_data(self) -> str:
        memory_message = ''
        for record in self.__data:
            memory_message += ("{0}) {1} {2} {3} = {4}\n"
                               .format(record['index'], record['firstNumber'], record['operator'],
                                       record['secondNumber'], record['result']))
        return memory_message

    def __load_data(self):
        try:
            with open(self.__file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def __save_data(self):
        with open(self.__file_name, 'w') as file:
            json.dump(self.__data, file)
