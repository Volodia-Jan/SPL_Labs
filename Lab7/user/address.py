# Клас для представлення адреси
class Address:
    # Конструктор, який приймає вулицю, номер квартири, місто, поштовий індекс і гео
    def __init__(self, street, suite, city, zipcode, geo):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo = geo

    # Метод, який повертає рядкове представлення об'єкта
    def __str__(self):
        return f"Address(street={self.street}, suite={self.suite}, city={self.city}, zipcode={self.zipcode}, geo={self.geo})"
