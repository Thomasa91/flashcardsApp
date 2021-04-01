from app.src.utilities.logger import logger
import json


class User:

    def __init__(self, user_id: int, username: str, email: str, password: str, birthday: str):
        self.id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.birthday = birthday

        logger.debug(
            f"User with id:{self.id}, username:{self.username} has been created")

    def __del__(self):
        logger.debug(
            f"User with id:{self.id}, username:{self.username} has been destroyed")

    def get_details(self) -> list:
        return [self.id, self.username, self.email, self.password, self.birthday]

    def to_json(self) -> str:
        return json.dumps(self.__dict__)
