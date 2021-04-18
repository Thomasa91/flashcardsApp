from app.src import dbConn
from app.src.models.Deck import Deck
from typing import List, Optional

from app.src.utilities.logger import logger


conn = dbConn.get()


def create(user_id: int, name: str) -> Optional[Deck]:

    query = f"INSERT INTO deck (name, user_id) VALUES ('{name}', {user_id});"

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    deck_id = c.lastrowid

    if deck_id:
        logger.debug(
            f"Deck with id:{deck_id} has been saved into database successfully")
        return Deck(deck_id, user_id, name)

    logger.error("Saving deck into database failed")
    return None


def get_all() -> List[Deck]:

    query = "SELECT * FROM deck"

    c = conn.cursor()

    c.execute(query)

    decks = []

    for deck_data in c.fetchall():
        decks.append(Deck.create_from_database_data(deck_data))

    logger.debug(f"Retrieved {len(decks)} deck records from database")
    return decks


def get_by_id(deck_id: int) -> Optional[Deck]:

    query = f"SELECT * FROM deck WHERE deck_id = {deck_id};"

    c = conn.cursor()

    c.execute(query)

    deck_data = c.fetchone()

    if deck_data:
        logger.debug(f"Deck with id:{deck_id} found in database")
        return Deck.create_from_database_data(deck_data)

    logger.debug(f"User with id:{deck_id} not found in database")
    return None


def get_by_user_id(user_id: int) -> List[Deck]:

    query = f"SELECT * FROM deck WHERE user_id = {user_id};"

    c = conn.cursor()

    c.execute(query)

    decks = []

    for deck_data in c.fetchall():
        decks.append(Deck.create_from_database_data(deck_data))

    logger.debug(
        f"Retrieved {len(decks)} decks with user_id:{user_id} from database")
    return decks
