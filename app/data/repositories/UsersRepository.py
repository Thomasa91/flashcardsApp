from app.data import databaseConnection
from app.data.models.User import User

conn = databaseConnection.connect()
# TODO try to return dic instead of array OR return User object?


def create(name, email, password, birthday):
    return User.new_user(name, email, password, birthday)

def user(data):
    return User.user(data)


# TODO return array or return array of User objects
# TODO how to name methods fetchUsers/getUsers ?
def getAll():
    query = "SELECT * FROM user"

    c = conn.cursor()

    c.execute(query)
    
    users = []

    for user_data in c.fetchall():
        
        users.append(user(user_data))

    return users

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

def save(user: User):
    
    userName = user.username
    userEmail = user.email
    userPassword = user.password
    birthdate = user.birthday

    query = f"""INSERT INTO user (name, email, password, date_of_birth) 
                    VALUES ('{userName}', '{userEmail}', '{userPassword}', '{birthdate}');"""

    c = conn.cursor()

    c.execute(query)

    conn.commit()

    return c.lastrowid
