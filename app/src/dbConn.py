import sqlite3
from sqlite3 import Error
from app.src.utilities.logger import logger
import time
from app.config import app_config


INITIAL_SLEEP_TIME = 2
MAX_SLEEP_TIME = 30
SLEEP_INTERVAL = 2
SLEEP_INCREASE_VALUE = 2


def connect():

    time_until_reconnect = INITIAL_SLEEP_TIME

    while(True):
        try:
            # SQLite objects created in a thread can only be used in that same thread.
            # tech_same_thread=False repaired it
            connection = sqlite3.connect(
                database=app_config.DATABASE_PATH, check_same_thread=False)
            logger.debug("Successfully connected to database")

            return connection

        except Error as e:
            logger.critical("Connection to database failed", exc_info=True)

            for seconds in range(time_until_reconnect, 0, -SLEEP_INTERVAL):
                logger.info(f"Reconnecting in {seconds} seconds")
                time.sleep(SLEEP_INTERVAL)

        if time_until_reconnect < MAX_SLEEP_TIME:
            time_until_reconnect += SLEEP_INCREASE_VALUE


conn = connect()


def get():
    return conn
