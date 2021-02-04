from app.data.repositories.UsersRepository import user
from app.data.repositories import CardsRepository

class Deck:


    def __init__(self, id, user_id, name):
        
        self.id = id
        self.user_id = user_id
        self.name = name


    @classmethod
    def new_deck(cls, user_id, name):
        return cls(None, user_id, name)


    @classmethod
    def deck(cls, args):
        return cls(*args)


    def getCards(self):

        cards = CardsRepository.getCardsByDeckId(self.id)

        return cards
   