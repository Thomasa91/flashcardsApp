from typing import Optional, List
from sqlite3 import Error
from app.src import dbConn
from app.src.models.User import User

from app.src.utilities.logger import logger
from app.src.models.User import User

conn = dbConn.get()


def create(username: str, email: str, password: str, birthday: str) -> Optional[User]:

    query = f"""INSERT INTO user (username, email, password, birthday) 
            VALUES ('{username}', '{email}', '{password}', '{birthday}');"""

    c = conn.cursor()

    try:
        c.execute(query)
    except Error as error:
        logger.error("User has not been saved", exc_info=True)
        return None

    conn.commit()
    
    user_id = c.lastrowid

    if user_id:

        logger.debug(
            f"User with id:{user_id} username:{username} has been created")
        return User(user_id, username, email, password, birthday)

    logger.error(f"Saving user {username} into database failed")
    return None


def get_all() -> List[User]:

    query = "SELECT * FROM user"

    c = conn.cursor()

    c.execute(query)

    users = []

    for user_data in c.fetchall():

        users.append(User.create_from_list(user_data))

    logger.debug(f"Retrieved {len(users)} user records from database")
    return users


def get_by_id(user_id: int) -> Optional[User]:

    query = f"SELECT * FROM user WHERE user_id = '{user_id}';"

    c = conn.cursor()

    c.execute(query)

    user_data = c.fetchone()

    if user_data:

        logger.debug(f"User with id:{user_id} found in database")
        return User.create_from_list(user_data)

    logger.debug(f"User with id:{user_id} not found in database")
    return None


def get_by_username(username: str) -> Optional[User]:

    query = f"SELECT * FROM user WHERE username = '{username}';"

    c = conn.cursor()

    c.execute(query)

    user_data = c.fetchone()

    if user_data:
        logger.debug(f"User with username:{username} found in database")
        return User.create_from_list(user_data)

    logger.debug(f"User with username:{username} not found in database")
    return None


def get_by_email(email: str) -> Optional[User]:

    query = f"SELECT * FROM user WHERE email = '{email}';"

    c = conn.cursor()

    c.execute(query)

    user_data = c.fetchone()

    if user_data:
        logger.debug(f"User with email:{email} found in database")
        return User.create_from_list(user_data)

    logger.debug(f"User with id:{email} not found in database")
    return None


def get_by_username_email(username: str, email: str) -> Optional[User]:

    query = f"SELECT * FROM user WHERE username = '{username}' AND email = '{email}';"

    c = conn.cursor()

    c.execute(query)

    user_data = c.fetchone()

    if user_data:
        logger.debug(
            f"User with username:{username} and email:{email}found in database")
        return User.create_from_list(user_data)

    logger.debug(
        f"User with username:{username} and email:{email} not found in database")
    return None
