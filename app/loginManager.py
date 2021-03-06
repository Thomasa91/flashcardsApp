from typing import Dict
from flask import session


from app.src.utilities.logger import logger
from app.src.repositories import UsersRepository
from app.src.utilities.decorators import template_function

from app.src.utilities.crypto import hash_password

import json


def authenticate(username, password) -> bool:
    user = UsersRepository.get_by_username(username)

    if user:
        if user.password == hash_password(password):
            logger.debug("User is authenticated and logged into session")
            session['user'] = user.to_json()
            return True
    
    logger.error("User is not authenticated")
    return False



@template_function
def is_authenticated() -> bool:
    return 'user' in session


def logout_user() -> None:
    return session.pop('user', None)


@template_function
def get_id() -> int:
    return json.loads(session['user'])['user_id']


@template_function
def get_username() -> str:
    return json.loads(session['user'])['username']


@template_function
def get_details() -> Dict:
    return json.loads(session['user'])
