from app.data import databaseConnection
from app.data.models.User import User

# TODO i make connection here what means that it creates connection when app starts, it happens to all repositories where I have 3 different connections how i can change it and where i should close that connections I haven't implemented it yet.

conn = databaseConnection.connect()


def create(name, email, password, birthday):

        
    name = name
    email = email
    password = password
    birthday = birthday
    
    query = f"""INSERT INTO user (name, email, password, date_of_birth) 
                    VALUES ('{name}', '{email}', '{password}', '{birthday}');"""

    conn = databaseConnection.connect()

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    if c.lastrowid:
        return True
    
    return False


def user(data):
    return User.user(data)


def getAll():
    query = "SELECT * FROM user"

    c = conn.cursor()

    c.execute(query)
    
    users = []

    for user_data in c.fetchall():
        
        users.append(user(user_data))

    return users


def getByEmailUsername():
    return "huj"

    
def getById(user_id):
    query = f"SELECT * FROM user WHERE user_name = '{user_id}';"

    c = conn.cursor()

    c.execute(query)
    
    return user(c.fetchone())


def getByName(username):
    
    query = f"SELECT * FROM user WHERE user_name = '{username}';"

    c = conn.cursor()

    c.execute(query)
    
    return user(c.fetchone())

# WHAT RETURN WHEN THERE IS NO USER IN DATABASE
def getByEmail(email):

    query = f"SELECT * FROM user WHERE user_email = '{email}';"

    c = conn.cursor()

    c.execute(query)

    dbUser = c.fetchone()

    if dbUser:
        return user(dbUser)

    return False

def getByEmailUsername(name, email):

    query = f"SELECT * FROM user WHERE name = '{name}' AND email = '{email}';"

    c = conn.cursor()

    c.execute(query)

    if c.fetchone:
        return user(c.fetchone)
    
    return False
