from os import path
import sqlite3
import pathlib
from sqlite3 import Error
from app.utilities.logger import logger
from flask import request

from app.config import app_config


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
