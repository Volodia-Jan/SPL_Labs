class FileHandler:
    @staticmethod
    def save_to_file(filename: str, content):
        try:
            with open(f"{filename}.txt", 'w') as file:
                for line in content:
                    file.write(str(line) + "\n")
            print(f"Object saved successfully to {filename}.txt")
        except Exception as e:
            print(f"Error occurred while saving: {e}")
