from app import logger

deck_logger = logger.getChild(__name__)


class Deck:
    def __init__(self, deck_id: int, user_id: int, name: str):

        self.id = deck_id
        self.user_id = user_id
        self.name = name

        deck_logger.debug(f"Deck with id {self.id} has been created") 
    
    def __del__(self):
        deck_logger.debug(f"Deck with id {self.id} has been destroyed")