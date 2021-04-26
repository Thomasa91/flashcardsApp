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
        logger.debug(f"Authenticating a user, username {username} exists")
        logger.debug(f"Authenticating a user, username {username} checking password")
        if user.password == hash_password(password):
            session['user'] = user.to_json()
            logger.debug(f"User {username} is authenticated and session is created")
            return True

        logger.error("Authenticating a user, invalid password")

    else:

        logger.error(
            "Authenticating a user, username does not exists")

    logger.error("Authenticating a user, user is not authenticated")
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
