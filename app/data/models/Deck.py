from app.logs.logger import logger


class Deck:
    def __init__(self, deck_id: int, user_id: int, name: str):

        self.id = deck_id
        self.user_id = user_id
        self.name = name
        logger.debug(
            f"Deck with id {self.id}, user_id:{self.user_id}, name:{self.name} has been created")

    def __del__(self):
        logger.debug(
            f"Deck with id {self.id}, user_id:{self.user_id}, name:{self.name} has been destroyed")
