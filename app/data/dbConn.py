import sqlite3
from sqlite3 import Error
from app.logs.logger import logger


from app import app_config
from app import app

def connect():

    try:
        # SQLite objects created in a thread can only be used in that same thread.
        # tech_same_thread=False repaired it
        connection = sqlite3.connect(app_config.DATABASE_PATH, check_same_thread=False)

        logger.debug("Successfully connected to database")
        return connection

    except Error as e:
        logger.critical("Connection to database failed", exc_info=True)        
        

conn = connect()


def get():
    return conn
