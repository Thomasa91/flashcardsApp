from app.data import dbConn
from app.data.models.Deck import Deck
from typing import List, Optional

conn = dbConn.get()


def create(user_id: int, name: str) -> Optional[Deck]:

    query = f"INSERT INTO deck (name, user_id) VALUES ('{name}', {user_id});"

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    deck_id = c.lastrowid

    if deck_id:
        return Deck(deck_id, user_id, name)

    return None


def get_all() -> List[Deck]:

    query = "SELECT * FROM deck"

    c = conn.cursor()

    c.execute(query)

    decks = []

    for deck_data in c.fetchall():
        decks.append(Deck(*deck_data))
    
    return decks


def get_by_id(deck_id: int) -> Optional[Deck]:

    query = f"SELECT * FROM deck WHERE deck_id = {deck_id};"

    c = conn.cursor()

    c.execute(query)

    deck_details = c.fetchone()

    if deck_details:
        return Deck(*deck_details)
    
    return None


def get_by_user_id(user_id: int) -> List[Deck]:

    query = f"SELECT * FROM deck WHERE user_id = {user_id};"

    c = conn.cursor()

    c.execute(query)
    
    decks = []

    for deck_details in c.fetchall():
        decks.append(Deck(*deck_details))

    return decks
