from typing import Optional


class Card:

    def __init__(self, card_id: Optional[int], deck_id: int, word: str, translation: str):
        self.id = card_id
        self.deck_id = deck_id
        self.word = word
        self.translation = translation

    @classmethod
    def new_card(cls, deck_id: int, word: str, translation: str):
        return cls(None, deck_id, word, translation)

    @classmethod
    def card(cls, args: list):
        return cls(*args)
