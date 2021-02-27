import re
import json
from app.data.repositories import UsersRepository


class User:

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


    def getDetails(self):

        return [self.id, self.username, self.email, self.password, self.birthday]


    def ifExists(self):
        return UsersRepository.fetchUserByEmail(self.email)


    def to_json(self):
        return json.dumps(self.__dict__)