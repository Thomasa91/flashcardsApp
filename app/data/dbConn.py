import sqlite3
from sqlite3 import Error
from app import logger

db_logger = logger.getChild(__name__)

from app import app_config


def connect():

    try:
        # SQLite objects created in a thread can only be used in that same thread.
        # tech_same_thread=False repaired it
        connection = sqlite3.connect(app_config.DATABASE_PATH, check_same_thread=False)

        db_logger.debug("Successfully connected to database")
        return connection

    except Error as e:
        db_logger.critical("Connection to database failed", exc_info=True)        


conn = connect()


def get():
    return conn
