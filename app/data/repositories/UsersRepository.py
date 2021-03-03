from typing import Optional, List

from app.data import dbConn
from app.data.models.Deck import Deck
from app.data.models.User import User


conn = dbConn.get()


def create(name: str, email: str, password: str, birthday: str) -> bool:
  
    query = f"""INSERT INTO user (name, email, password, date_of_birth) 
                    VALUES ('{name}', '{email}', '{password}', '{birthday}');"""

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    if c.lastrowid:
        return True

    return False


def user(data: list) -> Optional[User]:
    return User.user(data)


def get_all() -> List[User]:

    query = "SELECT * FROM user"

    c = conn.cursor()

    c.execute(query)
    
    users = []

    for user_data in c.fetchall():
        
        users.append(user(user_data))

    return users

    
def get_by_id(user_id: int) -> Optional[User]:

    query = f"SELECT * FROM user WHERE user_name = '{user_id}';"

    c = conn.cursor()

    c.execute(query)
    
    user_details = c.fetchone()

    if user_details:
        return user(c.fetchone()) 

    return None


def get_by_name(username: str) -> Optional[User]:
    
    query = f"SELECT * FROM user WHERE user_name = '{username}';"

    c = conn.cursor()

    c.execute(query)
    
    user_details = c.fetchone()

    if user_details:
        return user(user_details)
    
    return None


def get_by_email(email: str) -> Optional[User]:

    query = f"SELECT * FROM user WHERE user_email = '{email}';"

    c = conn.cursor()

    c.execute(query)

    user_details = c.fetchone()

    if user_details:
        return user(user_details)

    return None


def get_by_username_email(username, email) -> Optional[User]:

    query = f"SELECT * FROM user WHERE name = '{username}' AND email = '{email}';"

    c = conn.cursor()

    c.execute(query)

    user_details = c.fetchone()

    if user_details:
        return user(user_details)
    
    return None
