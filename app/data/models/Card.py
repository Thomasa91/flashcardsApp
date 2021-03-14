from app import logger

card_logger = logger.getChild(__name__)

class Card:

    def __init__(self, card_id: int, deck_id: int, word: str, translation: str):
        self.id = card_id
        self.deck_id = deck_id
        self.word = word
        self.translation = translation

        card_logger.debug(f"Card with id {self.id} has been created")

    def __del__(self):
        card_logger.debug(f"Card with id {self.id} has been destroyed")