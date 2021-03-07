import sqlite3
from sqlite3 import Error

from app import app_config


def connect():

    try:
        # SQLite objects created in a thread can only be used in that same thread.
        # tech_same_thread=False repaired it
        connection = sqlite3.connect(app_config.DATABASE_PATH, check_same_thread=False)
        print(sqlite3.version)

        return connection

    except Error as e:
        print(e)


conn = connect()


def get():
    return conn
