class FileHelper:
    def __init__(self, file_name):
        self.__file_name = file_name

    def save_in_file(self, content):
        try:
            with open(self.__file_name, "w") as f:
                f.write(content)
        except FileNotFoundError:
            print(f"File not fount by name: {self.__file_name}")
