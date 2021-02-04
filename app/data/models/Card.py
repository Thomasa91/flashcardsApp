class Card:

    def __init__(self, id, deck_id, word, translation ):
        self.id = id
        self.deck_id = deck_id
        self.word = word
        self.translation = translation


    @classmethod
    def new_card(cls, deck_id, word, translation):
        return cls(None, deck_id, word, translation)

    @classmethod
    def card(cls, args):
        return cls(*args)