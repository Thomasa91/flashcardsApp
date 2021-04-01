from typing import Optional, List

from app.src import dbConn
from app.src.models.User import User

from app.src.utilities.logger import logger


conn = dbConn.get()


def create(name: str, email: str, password: str, birthday: str) -> Optional[User]:

    query = f"""INSERT INTO user (name, email, password, date_of_birth) 
            VALUES ('{name}', '{email}', '{password}', '{birthday}');"""

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    user_id = c.lastrowid

    if user_id:

        logger.debug(f"User with id:{user_id} name:{name} has been created")
        return User(user_id, name, email, password, birthday)

    logger.error(f"Saving user {name} into database failed")
    return None


def get_all() -> List[User]:

    query = "SELECT * FROM user"

    c = conn.cursor()

    c.execute(query)

    users = []

    for user_data in c.fetchall():

        users.append(User(*user_data))

    logger.debug(f"Retrieved {len(users)} user records from database")
    return users


def get_by_id(user_id: int) -> Optional[User]:

    query = f"SELECT * FROM user WHERE user_name = '{user_id}';"

    c = conn.cursor()

    c.execute(query)

    user_details = c.fetchone()

    if user_details:

        logger.debug(f"User with id:{user_id} found in database")
        return User(*user_details)

    logger.debug(f"User with id:{user_id} not found in database")
    return None


def get_by_name(username: str) -> Optional[User]:

    query = f"SELECT * FROM user WHERE name = '{username}';"

    c = conn.cursor()

    c.execute(query)

    user_details = c.fetchone()

    if user_details:
        logger.debug(f"User with username:{username} found in database")
        return User(*user_details)

    logger.debug(f"User with username:{username} not found in database")
    return None


def get_by_email(email: str) -> Optional[User]:

    query = f"SELECT * FROM user WHERE email = '{email}';"

    c = conn.cursor()

    c.execute(query)

    user_details = c.fetchone()

    if user_details:
        logger.debug(f"User with email:{email} found in database")
        return User(*user_details)

    logger.debug(f"User with id:{email} not found in database")
    return None


def get_by_username_email(username: str, email: str) -> Optional[User]:

    query = f"SELECT * FROM user WHERE name = '{username}' AND email = '{email}';"

    c = conn.cursor()

    c.execute(query)

    user_details = c.fetchone()

    if user_details:
        logger.debug(
            f"User with username:{username} and email:{email}found in database")
        return User(*user_details)

    logger.debug(
        f"User with username:{username} and email:{email} not found in database")
    return None
