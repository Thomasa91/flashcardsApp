from app.data import dbConn
from app.data.models.Deck import Deck
from typing import List, Optional

from app.utilities.logger import logger


conn = dbConn.get()


def create(user_id: int, name: str) -> Optional[Deck]:

    query = f"INSERT INTO deck (name, user_id) VALUES ('{name}', {user_id});"

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    deck_id = c.lastrowid

    if deck_id:
        logger.debug(
            "Deck with id:{deck_id} has been saved into database successfully ")
        return Deck(deck_id, user_id, name)

    logger.error("Saving deck into database failed")
    return None


def get_all() -> List[Deck]:

    query = "SELECT * FROM deck"

    c = conn.cursor()

    c.execute(query)

    decks = []

    for deck_data in c.fetchall():
        decks.append(Deck(*deck_data))

    logger.debug(f"Retrieved {len(decks)} deck recrods from database")
    return decks


def get_by_id(deck_id: int) -> Optional[Deck]:

    query = f"SELECT * FROM deck WHERE deck_id = {deck_id};"

    c = conn.cursor()

    c.execute(query)

    deck_details = c.fetchone()

    if deck_details:
        logger.debug(f"Deck with id:{deck_id} found in database")
        return Deck(*deck_details)

    logger.debug(f"User with id:{deck_id} not found in database")
    return None


def get_by_user_id(user_id: int) -> List[Deck]:

    query = f"SELECT * FROM deck WHERE user_id = {user_id};"

    c = conn.cursor()

    c.execute(query)

    decks = []

    for deck_details in c.fetchall():
        decks.append(Deck(*deck_details))

    logger.debug(f"Retrieved {len(decks)} decks with user_id:{user_id} from database")
    return decks
