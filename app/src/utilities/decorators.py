from flask import session, redirect
from flask.helpers import url_for
from flask import session, redirect, url_for
from app.src.utilities.logger import logger

def login_required(func: object):
    def wrapper_login_required(*args):
        if 'user' not in session:
            logger.info("User is not authenticated, redirecting to '\login' route")
            return redirect(url_for('login'))
        logger.info({"User is authenticated"})
        func(*args)
    
    return wrapper_login_required

# TODO implement body for the function
def admin_required(func: object):
    def wrapper_admin_required(*args):
        return None
    
    return wrapper_admin_required