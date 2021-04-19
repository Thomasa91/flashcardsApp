from app.src.utilities.logger import logger
from typing import List, Any

class Card:

    def __init__(self, card_id: int, deck_id: int, word: str, translation: str):
        self.card_id = card_id
        self.deck_id = deck_id
        self.word = word
        self.translation = translation

        logger.debug(
            f"Card with id:{self.card_id}, deck_id:{self.deck_id}, word:{self.word}, translation{self.translation} has been created")

    @classmethod
    def create_from_list(cls, data: List[Any]):
        return cls(*data[:-2])

    def __del__(self):
        logger.debug(
            f"Card with id:{self.card_id}, deck_id:{self.deck_id}, word:{self.word}, translation{self.translation} has been destroyed")
