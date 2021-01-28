import re
from app.data.repositories import UsersRepository


class User:
    # TODO should i have validation methods here or to implement them in another way ?
    # TODO when i create a new user I don't have id, what to do with it
    def __init__(self, username, email, password, birthDay):
        self.id = None
        self.username = username
        self.email = email
        self.password = password
        self.birthDay = birthDay
    
    
    def __init__(self, *data):
        self.id = data[0]
        self.username = data[1]
        self.email = data[2]
        self.password = data[3]
        self.birthDay = data[4]

    def validateEmail(self):

        pattern = r".+@\w+.\w+"

        return re.match(pattern, self.email)


    def validatePassword(self):

        password = self.password

        # at least one cappital letter
        capitalLetter = r"[A-Z]+"
        # at least one small letter
        smallLetter = r"[a-z]+"
        # at least one number
        oneNumber = r"\d+"
        # min 8 characters, max 20
        numberOfCharacters = r"\.{8, 20}"

        return re.match(capitalLetter, password) and re.match(smallLetter, password) and re.match(oneNumber, password) and re.match(numberOfCharacters, password)
    
    def ifUserExists(self):

        if(UsersRepository.fetchUserByName(self.username)) or UsersRepository.fetchUserByEmail(self.email):
            return True

        return False

    def saveUserToDataBase(self):
        if self.ifUserExists():
            return False

        return UsersRepository.saveUser(self)
