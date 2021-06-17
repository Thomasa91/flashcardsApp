from flask import Flask
from app.src.repositories import UsersRepository
from app.src.models.User import User


app = Flask(__name__)
app.secret_key = 'Tomibomi'

from app.src.utilities import loginManager

from app import authentication_views
from app import views
from app import admin_views