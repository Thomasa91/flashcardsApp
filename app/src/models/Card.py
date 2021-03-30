from app.utilities.logger import logger


class Card:

    def __init__(self, card_id: int, deck_id: int, word: str, translation: str):
        self.id = card_id
        self.deck_id = deck_id
        self.word = word
        self.translation = translation

        logger.debug(
            f"Card with id:{self.id}, deck_id:{self.deck_id}, word:{self.word}, translation{self.translation} has been created")

    def __del__(self):
        logger.debug(
            f"Card with id:{self.id}, deck_id:{self.deck_id}, word:{self.word}, translation{self.translation} has been destroyed")
