import re
import json
from app.data.repositories import UsersRepository


class User:
    # TODO should i have validation methods here or to implement them in another way ?
    # TODO when i create a new user I don't have id, what to do with it
    # TODO crypt the password
    def __init__(self, id, username, email, password, birthday):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.birthday = birthday

    
    @classmethod
    def new_user(cls, username, email, password, birthday):
        return cls(None, username, email, password, birthday)


    @classmethod
    def user(cls, args):
        return cls(*args)

    # OF COURSE IT DOESN'T WORK....
    def validateEmail(self):

        pattern = r"\.+@\w+.\w+"

        # return re.match(pattern, self.email)

        return True


    # VALIDATION DOESN'T WORK REFACOTR IT LATER
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

        # return re.match(capitalLetter, password) and re.match(smallLetter, password) and re.match(oneNumber, password) and re.match(numberOfCharacters, password)

        return True

    def getUserDetails(self):

        return [self.id, self.username, self.email, self.password, self.birthday]


    def ifUserExists(self):
        return UsersRepository.fetchUserByEmail(self.email)

# RETURN JSON
    def to_json(self):
        return json.dumps(self.__dict__)