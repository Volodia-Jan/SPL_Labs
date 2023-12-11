# Клас для представлення користувача
class User:
    # Конструктор, який приймає id, firstname, lastname, email, birthDate, login, address, phone, website і company
    def __init__(self, id, firstname, lastname, email, birth_date, login, address, phone, website, company):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.birth_date = birth_date
        self.login = login
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company

    # Метод, який повертає рядкове представлення об'єкта
    def __str__(self):
        return f"User(id={self.id}, firstname={self.firstname}, lastname={self.lastname}, email={self.email}, birthDate={self.birth_date}, login={self.login}, address={self.address}, phone={self.phone}, website={self.website}, company={self.company})"
