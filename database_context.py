import sqlite3
from sqlite3 import Error
import app_config


def connect():

    try:
        conn = sqlite3.connect(app_config.DATABASE_PATH)
        print(sqlite3.version)

        return conn

    except Error as e:
        print(e)
