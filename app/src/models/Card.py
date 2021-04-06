from app.src.utilities.logger import logger


class Card:

    def __init__(self, card_id: int, deck_id: int, word: str, translation: str, created_at: str, updated_at: str):
        self.card_id = card_id
        self.deck_id = deck_id
        self.word = word
        self.translation = translation
        self.created_at = created_at
        self.updated_at = updated_at

        logger.debug(
            f"Card with id:{self.card_id}, deck_id:{self.deck_id}, word:{self.word}, translation{self.translation} has been created")

    def __del__(self):
        logger.debug(
            f"Card with id:{self.card_id}, deck_id:{self.deck_id}, word:{self.word}, translation{self.translation} has been destroyed")
