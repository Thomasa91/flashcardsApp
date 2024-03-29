from typing import List, Optional
from sqlite3 import Error

from app.src import dbConn
from app.src.models.Card import Card

from app.src.utilities.logger import logger


conn = dbConn.get()

#TODO implement exception handling


def create(deck_id: int, word: str, translation: str) -> Optional[Card]:

    query = f"INSERT INTO card (deck_id, word, translation) VALUES ({deck_id}, '{word}', '{translation}');"

    c = conn.cursor()

    c.execute(query)
    conn.commit()

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

    for card_data in c.fetchall():
        cards.append(Card.create_from_list(card_data))

    logger.debug(f"Retrieved {len(cards)} card records from database")
    return cards


def get_by_deck_id(deck_id: int) -> List[Card]:

    query = f"SELECT * FROM card WHERE deck_id = {deck_id};"

    c = conn.cursor()

    c.execute(query)

    cards = []

    for card_data in c.fetchall():
        cards.append(Card.create_from_list(card_data))

    logger.debug(
        f"Retrieved {len(cards)} cards with deck_id:{deck_id} from database")
    return cards


def get_by_id(card_id: int) -> Optional[Card]:

    query = f"SELECT * FROM card WHERE card_id = {card_id};"

    c = conn.cursor()

    c.execute(query)

    card_data = c.fetchone()

    if card_data:
        logger.debug(f"Card with id:{card_id} found in database")
        return Card.create_from_list(card_data)

    logger.debug(f"Card with id:{card_id} not found in database")
    return None


def delete(card_id: int) -> bool:
    
    query = f"DELETE FROM card WHERE card_id = {card_id};"

    c = conn.cursor()

    c.execute(query)
    
    conn.commit()
    
    if c.rowcount:
        logger.debug(f"Card with id {card_id} has been removed")        
        return True

    logger.debug(f"Deleting a card with id {card_id} has not finished successfully")
    return False


def update(id: int, word: str, translation: str):

    query = f"UPDATE card SET word = '{word}', translation = '{translation}' WHERE card_id = {id};"

    c = conn.cursor()
    c.execute(query)

    conn.commit()

    if c.rowcount:
        logger.debug(f"Card with id {id} has been updated")
        return True

    logger.debug(f"Updating a card with id {id} has not finished successfully")

    return False
