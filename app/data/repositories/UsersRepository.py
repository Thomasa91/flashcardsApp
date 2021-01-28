from app.data import databaseConnection
from app.data.models import User

conn = databaseConnection.connect()
# TODO try to return dic instead of array OR return User object?
def fetchUsers():
    query = "SELECT * FROM user"

    c = conn.cursor()

    c.execute(query)

    return c.fetchall()

def fetchUserById(user_id):
    query = f"SELECT * FROM user WHERE user_name = '{user_id}';"

    c = conn.cursor()

    c.execute(query)
    
    return c.fetchone()


def fetchUserByName(username):
    
    query = f"SELECT * FROM user WHERE user_name = '{username}';"

    c = conn.cursor()

    c.execute(query)
    
    user = User(c.fetchone())

    if user.ifUserExists():
        return user

    return None


def fetchUserByEmail(email):

    query = f"SELECT * FROM user WHERE user_email = '{email}';"

    c = conn.cursor()

    c.execute(query)

    return c.fetchone()


def saveUser(user: User):
    
    userName = user.username
    userEmail = user.email
    userPassword = user.password
    birthDate = user.birthDay

    query = f"""INSERT INTO user (user_name, user_email, user_password, date_of_birth) 
                    VALUES ('{userName}', '{userEmail}', '{userPassword}', '{birthDate}');"""

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    return c.lastrowid()
