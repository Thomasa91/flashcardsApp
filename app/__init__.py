from flask import Flask, session

app = Flask(__name__)
app.secret_key = "tomibomi"

from app import data
from app import authentication_views
from app.data.models import User

user = User()