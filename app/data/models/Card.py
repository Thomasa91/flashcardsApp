class Card:

    def __init__(self, card_id: int, deck_id: int, word: str, translation: str):
        self.id = card_id
        self.deck_id = deck_id
        self.word = word
        self.translation = translation
