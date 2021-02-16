from app.data import databaseConnection
from app.data.models.Card import Card


conn = databaseConnection.conn


def create(deck_id, word, translation):

    deck_id = deck_id
    word = word
    translation = translation

    query = f"INSERT INTO card (deck_id, word, translation) VALUES ({deck_id}, '{word}', '{translation}');"

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    if c.lastrowid:
        return True
    
    return False


def card(data):
    return Card.card(data)


def getAll():

    query = "SELECT * FROM card"

    c = conn.cursor()

    c.execute(query)

    cards = []

    for data in c.fetchall():
        cards.append(card(data))

    return cards


def getByDeckId(deck_id):

    query = f"SELECT * FROM card WHERE deck_id = {deck_id};"

    c = conn.cursor()

    c.execute(query)

    cards = []

    for card_data in c.fetchall():
        cards.append(card(card_data))

    return cards


def getById(card_id):

    query = f"SELECT * FROM card WHERE card_id = {card_id};"

    c = conn.cursor()

    c.execute(query)

    return card(c.fetchone())
