from app.data.models.Deck import Deck
import json


class User:

    def __init__(self, user_id: int, username: str, email: str, password: str, birthday: str):
        self.id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.birthday = birthday

    def get_details(self) -> list:
        return [self.id, self.username, self.email, self.password, self.birthday]

    def to_json(self) -> str:
        return json.dumps(self.__dict__)
