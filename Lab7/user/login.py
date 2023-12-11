# Клас для представлення логіна
class Login:
    # Конструктор, який приймає uuid, username, password, md5, sha1 і registered
    def __init__(self, uuid, username, password, md5, sha1, registered):
        self.uuid = uuid
        self.username = username
        self.password = password
        self.md5 = md5
        self.sha1 = sha1
        self.registered = registered

    # Метод, який повертає рядкове представлення об'єкта
    def __str__(self):
        return f"Login(uuid={self.uuid}, username={self.username}, password={self.password}, md5={self.md5}, sha1={self.sha1}, registered={self.registered})"
