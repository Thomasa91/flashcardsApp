from typing import Dict
from flask import session

from app.src.models.User import User
from app.src.utilities.decorators import template_function

import json

# TODO change this module
def authenticate(user: User) -> None:
    session['user'] = user.to_json()


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
