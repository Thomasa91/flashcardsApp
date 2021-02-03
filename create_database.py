from app import app_config

# from app.data.models.User import User
# from app.data.models.Deck import Deck
# from app.data.models.Card import Card

from app.data.repositories import UsersRepository
from app.data.repositories import DecksRepository
from app.data.repositories import CardsRepository

import sqlite3
import random
import string

from sqlite3 import Error

# TODO remember to use later sqlite3 method execute(querry, [values])!!
CREATE_DECK_TABLE_SQL = """CREATE TABLE IF NOT EXISTS deck (
                            deck_id INTEGER PRIMARY KEY,
                            user_id INTEGER,
                            name TEXT,
                            FOREIGN KEY(user_id) REFERENCES user(user_id));"""

CREATE_CARD_TABLE_SQL = """CREATE TABLE IF NOT EXISTS card (
                            card_id INTEGER PRIMARY KEY,
                            deck_id INTEGER,
                            word TEXT,
                            translation TEXT,
                            FOREIGN KEY(deck_id) REFERENCES deck(deck_id));"""

CREATE_USERS_TABLE_SQL = """CREATE TABLE IF NOT EXISTS user (
                            user_id INTEGER PRIMARY KEY,
                            name TEXT,
                            email TEXT,
                            password TEXT,
                            date_of_birth TEXT);"""

MIN_NUMBER_OF_LETTERS = 5
MAX_NUMBER_OF_LETTERS = 15


MIN_NUMBER_OF_WORDS = 7
MAX_NUMBER_OF_WORDS = 15

MIN_NUMBER_OF_CARDS = 30
MAX_NUMBER_OF_CARDS = 60

MIN_NUMBER_OF_DECKS = 3
MAX_NUMBER_OF_DECKS = 6

MIN_NUMBER_OF_USERS = 1
MAX_NUMBER_OF_USERS = 4


def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


# CREATE TABLES
def create_table(conn, sql):
    c = conn.cursor()
    
    c.execute(sql)

    conn.commit()


# GENERATE DATA
def generate_random_word():

    length = random.randint(MIN_NUMBER_OF_LETTERS, MAX_NUMBER_OF_LETTERS)
    return ''.join(random.choice(string.ascii_letters) for x in range(1, length))


def generate_random_translation():

    amount_of_words = random.randint(MIN_NUMBER_OF_WORDS, MAX_NUMBER_OF_WORDS)

    return ' '.join(generate_random_word() for x in range(1, amount_of_words))


def generate_decks():

    users_id = [user.id for user in UsersRepository.fetchUsers()]

    number_of_decks = random.randint(MIN_NUMBER_OF_DECKS, MAX_NUMBER_OF_DECKS)

    for x in range(1, number_of_decks):
        
        name = generate_random_word()
        user_id = random.choice(users_id)

        deck = DecksRepository.createDeck(user_id, name)
        DecksRepository.saveToDataBase(deck)

def generate_cards():
    
    number_of_cards = random.randint(MIN_NUMBER_OF_CARDS, MAX_NUMBER_OF_CARDS)
    
    decks_id = [deck.deck_id for deck in DecksRepository.fetch_decks()]

    for x in range(1, number_of_cards + 1):

        word = generate_random_word()
        translation = generate_random_translation()
        deck_id = random.choice(decks_id)    
        card = CardsRepository.createCard(deck_id, word, translation)
        CardsRepository.saveCardToDataBase(card)
 
# Generate users and save them into database
def generate_users():
    
    number_of_users = random.randint(MIN_NUMBER_OF_USERS, MAX_NUMBER_OF_USERS)

    for x in range(1, number_of_users + 1):
        name = generate_random_word()
        email = generate_random_word(  ) + "@gmail.com"
        password = generate_random_word()
        birthday = str(random.randint(1970, 2010))

        user = UsersRepository.createUser(name, email, password, birthday)
        UsersRepository.saveUser(user)

# INSEsaveUser(RT DATA INTO TABLES
# def psaveUser(ut_decks_into_table(conn, decks, users):
#     c = conn.cursor()
#     number_of_users = len(users)

#     query = "INSERT INTO deck (name, user_id) VALUES"

#     for deck in decks:
        
#         values = f"('{deck}', {random.randint(1, number_of_users)});"

#         c.execute(' '.join([query, values]))

#     conn.commit()

#     return c.lastrowid

# def put_cards_into_table(conn, number_of_decks):

#     c = conn.cursor()

#     query = "INSERT INTO card (word, deck_id, translation) VALUES"

#     cards = generate_cards()

#     for card_index in range(0, len(cards)):
#         word = cards[card_index]["word"]
#         translation = cards[card_index]["translation"]
#         deck_index = random.randint(1, number_of_decks)
#         values = f"('{word}', {deck_index}, '{translation}');"

#         c.execute(' '.join([query, values]))

#     conn.commit()

#     return c.lastrowid

# def put_user_into_table(conn, users):

#     c = conn.cursor()

#     querry = "INSERT INTO user (name, email, password, date_of_birth) VALUES"

#     for user in users:

#         values = ', '.join(["'" + value + "'" for value in ussaveUser(er])
#         values = ''.join(["(", values, ")", ";"])

#         c.execute(' '.join([querry, values]))

    
#     conn.commit()

#     return c.lastrowid


if __name__ == "__main__":
    conn = create_connection(app_config.DATABASE_PATH)

    create_table(conn, CREATE_DECK_TABLE_SQL)
    create_table(conn, CREATE_CARD_TABLE_SQL)
    create_table(conn, CREATE_USERS_TABLE_SQL)

    generate_users()
    generate_decks()
    generate_cards()
