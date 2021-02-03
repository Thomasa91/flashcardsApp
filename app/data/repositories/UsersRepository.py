from app.data import databaseConnection
from app.data.models.User import User

conn = databaseConnection.connect()
# TODO try to return dic instead of array OR return User object?


def createUser(name, email, password, birthday):
    return User.new_user(name, email, password, birthday)

def user(data):
    return User.user(data)


# TODO return array or return array of User objects
# TODO how to name methods fetchUsers/getUsers ?
def fetchUsers():
    query = "SELECT * FROM user"

    c = conn.cursor()

    c.execute(query)
    
    users = []

    for user_data in c.fetchall():
        
        users.append(user(user_data))

    return users

def fetchUserById(user_id):
    query = f"SELECT * FROM user WHERE user_name = '{user_id}';"

    c = conn.cursor()

    c.execute(query)
    
    return user(c.fetchone())


def fetchUserByName(username):
    
    query = f"SELECT * FROM user WHERE user_name = '{username}';"

    c = conn.cursor()

    c.execute(query)
    
    return user(c.fetchone())

# WHAT RETURN WHEN THERE IS NO USER IN DATABASE
def fetchUserByEmail(email):

    query = f"SELECT * FROM user WHERE user_email = '{email}';"

    c = conn.cursor()

    c.execute(query)

    user_from_data_base = c.fetchone()

    if user_from_data_base:
        return user(user_from_data_base)

    return False

def saveUser(user: User):
    
    userName = user.username
    userEmail = user.email
    userPassword = user.password
    birthdate = user.birthday

    query = f"""INSERT INTO user (user_name, user_email, user_password, date_of_birth) 
                    VALUES ('{userName}', '{userEmail}', '{userPassword}', '{birthdate}');"""

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    return c.lastrowid
