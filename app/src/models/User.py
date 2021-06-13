from app.src.utilities.logger import logger
from typing import List, Any
from flask_login import UserMixin
import json


class User(UserMixin):

    def __init__(self, user_id: int, username: str, email: str, password: str, birthday: str):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.birthday = birthday

        logger.debug(
            f"User with id:{self.user_id}, username:{self.username} has been created")

    @classmethod
    def create_from_list(cls, data: List[Any]):
        return cls(*data[:-2])

    def __del__(self):
        logger.debug(
            f"User with id:{self.user_id}, username:{self.username} has been destroyed")

    def get_details(self) -> list:
        return [self.user_id, self.username, self.email, self.password, self.birthday]

    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    def get_id(self):
        return self.user_id
