import sqlite3
from sqlite3 import Error
from app.src.utilities.logger import logger

from app.config import app_config

# TODO terminate server when conn to db failed or try to conn again
def connect():

    try:
        # SQLite objects created in a thread can only be used in that same thread.
        # tech_same_thread=False repaired it
        connection = sqlite3.connect(database=app_config.DATABASE_PATH, check_same_thread=False)
        logger.debug("Successfully connected to database")
        return connection

    except Error as e:
        logger.critical("Connection to database failed", exc_info=True)


conn = connect()


def get():
    return conn
