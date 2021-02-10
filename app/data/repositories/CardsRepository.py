from app.data import databaseConnection
from app.data.models.Card import Card


conn = databaseConnection.connect()


def create(deck_id, word, translation):
    return Card.new_card(deck_id, word, translation)

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

def save(card: Card):

    deck_id = card.deck_id
    word = card.word
    translation = card.translation


    query = f"INSERT INTO card (deck_id, word, translation) VALUES ({deck_id}, '{word}', '{translation}');"

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    return c.lastrowid