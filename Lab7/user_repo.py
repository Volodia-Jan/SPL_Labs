from Lab7.http_client import HttpClient
from Lab7.user import User


class UserRepository:
    BASE_URL = 'https://jsonplaceholder.org'

    def __init__(self):
        self.__http_client = HttpClient(UserRepository.BASE_URL)

    def get_all_users(self):
        return self.__http_client.get('/users')

    def get_user_by_id(self, user_id: int):
        return self.__http_client.get(f'/users/{user_id}')

    def create_user(self, user: User):
        return self.__http_client.post('/users', data=user)
