import sqlite3
import random
import string

from sqlite3 import Error

# TODO remember to use later sqlite3 method execute(querry, [values])!!
CREATE_DECK_TABLE_SQL = """CREATE TABLE IF NOT EXISTS deck (
                            deck_id INTEGER PRIMARY KEY,
                            name TEXT);"""

CREATE_CARD_TABLE_SQL = """CREATE TABLE IF NOT EXISTS card (
                            card_id INTEGER PRIMARY KEY,
                            deck_id INTEGER,
                            word TEXT,
                            translation TEXT,
                            FOREIGN KEY(deck_id) REFERENCES deck(deck_id));"""


MIN_NUMBER_OF_LETTERS = 5
MAX_NUMBER_OF_LETTERS = 15


MIN_NUMBER_OF_WORDS = 7
MAX_NUMBER_OF_WORDS = 15

MIN_NUMBER_OF_CARDS = 30
MAX_NUMBER_OF_CARDS = 60

MIN_NUMBER_OF_DECKS = 3
MAX_NUMBER_OF_DECKS = 6


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

    decks = []

    number_of_decks = random.randint(MIN_NUMBER_OF_DECKS, MAX_NUMBER_OF_DECKS)

    for x in range(1, number_of_decks):
        
        name = generate_random_word()
        decks.append(name)

    return decks


def generate_cards():
    cards = []
    
    amount_of_cards = random.randint(MIN_NUMBER_OF_CARDS, MAX_NUMBER_OF_CARDS)

    for x in range(1, amount_of_cards + 1):
        word = generate_random_word()
        translation = generate_random_translation()
        cards.append({"word" : word, "translation": translation})

    return cards


# INSERT DATA INTO TABLES
def put_decks_into_table(conn, decks):
    c = conn.cursor()
    query = "INSERT INTO deck (name) VALUES"

    for card_index in range(0, len(decks)):
        
        value = f"('{decks[card_index]}');"

        c.execute(' '.join([query, value]))

    conn.commit()

    return c.lastrowid

def put_cards_into_table(conn, number_of_decks):

    c = conn.cursor()

    query = "INSERT INTO card (word, deck_id, translation) VALUES"

    cards = generate_cards()

    for card_index in range(0, len(cards)):
        word = cards[card_index]["word"]
        translation = cards[card_index]["translation"]
        deck_index = random.randint(1, number_of_decks)
        values = f"('{word}', {deck_index}, '{translation}');"

        c.execute(' '.join([query, values]))

    conn.commit()

    return c.lastrowid


if __name__ == "__main__":
    conn = create_connection(r"app/database.db")

    create_table(conn, CREATE_DECK_TABLE_SQL)
    create_table(conn, CREATE_CARD_TABLE_SQL)

    decks = generate_decks()
    cards = generate_cards()
    
    put_decks_into_table(conn, decks)
    put_cards_into_table(conn, len(decks))
