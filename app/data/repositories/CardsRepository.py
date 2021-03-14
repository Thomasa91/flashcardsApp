from typing import List, Optional

from app.data import dbConn
from app.data.models.Card import Card

from app import logger

# TODO find shorter name of the variable
card_repo_logger = logger.getChild(__name__)

conn = dbConn.get()


def create(deck_id, word, translation) -> Optional[Card]:

    query = f"INSERT INTO card (deck_id, word, translation) VALUES ({deck_id}, '{word}', '{translation}');"

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    card_id = c.lastrowid

    if card_id:
        card_repo_logger.debug(f"Card with id {card_id} has been saved into database successfully")
        return Card(card_id, deck_id, word, translation)

    card_repo_logger.warning("Saving card into database failed")   
    return None


def get_all() -> List[Card]:

    query = "SELECT * FROM card"

    c = conn.cursor()

    c.execute(query)

    cards = []

    for data in c.fetchall():
        cards.append(Card(*data))

    card_repo_logger.debug("Retrieved all card records from database") 
    return cards


def get_by_deck_id(deck_id: int) -> List[Card]:

    query = f"SELECT * FROM card WHERE deck_id = {deck_id};"

    c = conn.cursor()

    c.execute(query)

    cards = []

    for card_data in c.fetchall():
        cards.append(Card(*card_data))

    card_repo_logger.debug(f"Retrieved cards with deck_id:{deck_id} from database")  
    return cards


def get_by_id(card_id: int) -> Optional[Card]:

    query = f"SELECT * FROM card WHERE card_id = {card_id};"

    c = conn.cursor()

    c.execute(query)

    card_details = c.fetchone()

    if card_details:
        card_repo_logger.debug(f"Card with id:{card_id} found in database")
        return Card(*card_details)

    card_repo_logger.debug(f"Card with id:{card_id} no found in database")
    return None
