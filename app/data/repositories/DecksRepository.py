from app.data.repositories.UsersRepository import user
from app.data import databaseConnection
from app.data.models.Deck import Deck


conn = databaseConnection.connect()


def createDeck(user_id, name):
    return Deck.new_deck(user_id, name)


def deck(data):
    return Deck.deck(data)


def fetch_decks():

    query = "SELECT * FROM deck"

    c = conn.cursor()

    c.execute(query)

    decks = []

    for deck_data in c.fetchall():
        decks.append(deck(deck_data))
    
    return decks

def fech_deck_by_id(id):

    query = f"SELECT * FROM deck WHERE deck_id = {id};"

    c = conn.cursor()

    c.execute(query)

    return deck(c.fetchone())


def fech_deck_by_user_id(id):

    query = f"SELECT * FROM deck WHERE user_id = {id};"

    c = conn.cursor()

    c.execute(query)

    return deck(c.fetchone())


def saveToDataBase(deck : Deck):
    name = deck.name
    username_id = deck.user_id

    query = f"INSERT INTO deck (name, user_id) VALUES ('{name}', {username_id});"

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    return c.lastrowid