# Клас для представлення компанії
class Company:
    # Конструктор, який приймає назву, слоган і сферу діяльності
    def __init__(self, name, catchPhrase, bs):
        self.name = name
        self.catchPhrase = catchPhrase
        self.bs = bs

    # Метод, який повертає рядкове представлення об'єкта
    def __str__(self):
        return f"Company(name={self.name}, catchPhrase={self.catchPhrase}, bs={self.bs})"
