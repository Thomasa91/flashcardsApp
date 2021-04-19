from flask import session, redirect
from flask.helpers import url_for
from flask import session, redirect, url_for
from flask.wrappers import Response
from app.src.utilities.logger import logger
from functools import wraps
from typing import Callable
from app import app


def login_required(func: Callable):
    @wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if 'user' not in session:
            logger.info(
                "User is not authenticated, redirecting to '\login' route")
            return redirect(url_for('login'))
        logger.info(f"User is authenticated")
        return func(*args, **kwargs)

    return wrapper_login_required


def template_function(func: Callable):
    app.jinja_env.globals[func.__name__] = func
    return func
