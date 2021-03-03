from typing import Optional
from app.data.repositories import CardsRepository


class Deck:

    def __init__(self, deck_id: Optional[int], user_id: int, name: str):
        
        self.id = deck_id
        self.user_id = user_id
        self.name = name
        self.cards = CardsRepository.get_by_deck_id(self.id)

    @classmethod
    def new_deck(cls, user_id: int, name: str):
        return cls(None, user_id, name)

    @classmethod
    def deck(cls, args: list):
        return cls(*args)
