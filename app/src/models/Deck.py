from app.src.utilities.logger import logger


class Deck:
    def __init__(self, deck_id: int, user_id: int, name: str, created_at: str, updated_at: str):

        self.deck_id = deck_id
        self.user_id = user_id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at

        logger.debug(
            f"Deck with id {self.deck_id}, user_id:{self.user_id}, name:{self.name} has been created")

    def __del__(self):
        logger.debug(
            f"Deck with id {self.deck_id}, user_id:{self.user_id}, name:{self.name} has been destroyed")
