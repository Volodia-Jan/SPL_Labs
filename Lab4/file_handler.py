class FileHandler:
    @staticmethod
    def save_to_file(ascii_art: str):
        save_file = input("Бажаєте зберегти ASCII-арт у файл? (y/n): ")
        if save_file == "y":
            file_name = input("Введіть назву файлу: ")
            with open(file_name, "w") as f:
                f.write(ascii_art)

    @staticmethod
    def load_from_file():
        file_name = input("Введіть назву файлу: ")
        try:
            with open(file_name, "r") as f:
                ascii_art = f.read()
                print(ascii_art)
        except FileNotFoundError:
            print("Файл не знайдено.")
