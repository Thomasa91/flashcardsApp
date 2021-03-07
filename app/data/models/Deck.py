from app.data.models.Card import Card


class Deck:
    def __init__(self, deck_id: int, user_id: int, name: str):

        self.id = deck_id
        self.user_id = user_id
        self.name = name
