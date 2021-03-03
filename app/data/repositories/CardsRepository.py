from typing import List, Optional

from app.data import dbConn
from app.data.models.Card import Card


conn = dbConn.get()


def create(deck_id, word, translation) -> bool:

    query = f"INSERT INTO card (deck_id, word, translation) VALUES ({deck_id}, '{word}', '{translation}');"

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    if c.lastrowid:
        return True

    return False


def card(data: list) -> Card:
    return Card.card(data)


def get_all() -> List[Card]:

    query = "SELECT * FROM card"

    c = conn.cursor()

    c.execute(query)

    cards = []

    for data in c.fetchall():
        cards.append(card(data))

    return cards


def get_by_deck_id(deck_id: int) -> List[Card]:

    query = f"SELECT * FROM card WHERE deck_id = {deck_id};"

    c = conn.cursor()

    c.execute(query)

    cards = []

    for card_data in c.fetchall():
        cards.append(card(card_data))

    return cards


def get_by_id(card_id: int) -> Optional[Card]:

    query = f"SELECT * FROM card WHERE card_id = {card_id};"

    c = conn.cursor()

    c.execute(query)

    card_details = c.fetchone()

    if card_details:
        return card(card_details)

    return None
