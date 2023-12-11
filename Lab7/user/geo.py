# Клас для представлення географічних координат
class Geo:
    # Конструктор, який приймає широту і довготу
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    # Метод, який повертає рядкове представлення об'єкта
    def __str__(self):
        return f"Geo(lat={self.lat}, lng={self.lng})"
