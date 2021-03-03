from app.data.repositories import DecksRepository
from typing import Optional
import json


class User:

    def __init__(self, user_id: Optional[int], username: str, email: str, password: str, birthday: str):
        self.id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.birthday = birthday
        self.decks = DecksRepository.get_by_user_id(self.id)
    
    @classmethod
    def new_user(cls, username: str, email: str, password: str, birthday: str):
        return cls(None, username, email, password, birthday)

    @classmethod
    def user(cls, args):
        return cls(*args)

    def get_details(self) -> list:

        return [self.id, self.username, self.email, self.password, self.birthday]

    def to_json(self) -> str:
        return json.dumps(self.__dict__)
