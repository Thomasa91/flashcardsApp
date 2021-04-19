from app.src.utilities.logger import logger
from typing import List

class Deck:
    def __init__(self, deck_id: int, user_id: int, name: str):

        self.deck_id = deck_id
        self.user_id = user_id
        self.name = name

        logger.debug(
            f"Deck with id {self.deck_id}, user_id:{self.user_id}, name:{self.name} has been created")

    @classmethod
    def create_from_array(cls, data: List):
        return cls(*data[:-2])

    def __del__(self):
        logger.debug(
            f"Deck with id {self.deck_id}, user_id:{self.user_id}, name:{self.name} has been destroyed")
