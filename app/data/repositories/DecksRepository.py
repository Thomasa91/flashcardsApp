from app.data import dbConn
from app.data.models.Deck import Deck
from typing import List, Optional

conn = dbConn.get()


def create(user_id: int, name: str) -> bool:

    query = f"INSERT INTO deck (name, user_id) VALUES ('{name}', {user_id});"

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    if c.lastrowi:
        return True

    return False


# TODO how to name that function in all Repositories
def deck(data) -> Deck:
    return Deck.deck(data)


def get_all() -> List[Deck]:

    query = "SELECT * FROM deck"

    c = conn.cursor()

    c.execute(query)

    decks = []

    for deck_data in c.fetchall():
        decks.append(deck(deck_data))
    
    return decks


def get_by_id(deck_id: int) -> Optional[Deck]:

    query = f"SELECT * FROM deck WHERE deck_id = {deck_id};"

    c = conn.cursor()

    c.execute(query)

    deck_details = c.fetchone()

    if deck_details:
        return deck(deck_details)
    
    return None


def get_by_user_id(user_id: int) -> List[Deck]:

    query = f"SELECT * FROM deck WHERE user_id = {user_id};"

    c = conn.cursor()

    c.execute(query)
    
    decks = []

    for deck_details in c.fetchall():
        decks.append(deck(deck_details))

    return decks
