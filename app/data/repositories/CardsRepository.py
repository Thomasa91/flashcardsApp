from typing import List, Optional

from app.data import dbConn
from app.data.models.Card import Card

from app.logs.logger import logger


conn = dbConn.get()


def create(deck_id: int, word: str, translation: str) -> Optional[Card]:

    query = f"INSERT INTO card (deck_id, word, translation) VALUES ({deck_id}, '{word}', '{translation}');"

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    conn.Error

    card_id = c.lastrowid

    if card_id:
        logger.debug(
            f"Card with id {card_id} has been saved into database successfully")
        return Card(card_id, deck_id, word, translation)

    logger.error("Saving card into database failed")
    return None


def get_all() -> List[Card]:

    query = "SELECT * FROM card"

    c = conn.cursor()

    c.execute(query)

    cards = []

    for data in c.fetchall():
        cards.append(Card(*data))

    logger.debug(f"Retrieved {len(cards)} card records from database")
    return cards


def get_by_deck_id(deck_id: int) -> List[Card]:

    query = f"SELECT * FROM card WHERE deck_id = {deck_id};"

    c = conn.cursor()

    c.execute(query)

    cards = []

    for card_data in c.fetchall():
        cards.append(Card(*card_data))

    logger.debug(f"Retrieved {len(cards)} cards with deck_id:{deck_id} from database")
    return cards


def get_by_id(card_id: int) -> Optional[Card]:

    query = f"SELECT * FROM card WHERE card_id = {card_id};"

    c = conn.cursor()

    c.execute(query)

    card_details = c.fetchone()

    if card_details:
        logger.debug(f"Card with id:{card_id} found in database")
        return Card(*card_details)

    logger.debug(f"Card with id:{card_id} not found in database")
    return None
