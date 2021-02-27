import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import connect
from app import app_config


def connect():

    #SQLite objects created in a thread can only be used in that same thread.
    #tech_same_thread=False repaired it
    try:
        conn = sqlite3.connect(app_config.DATABASE_PATH, check_same_thread=False)
        print(sqlite3.version)

        
        return conn

    except Error as e:
        print(e)

conn = connect()


def get():
    return conn

