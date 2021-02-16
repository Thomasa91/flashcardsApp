from flask import Flask, session

app = Flask(__name__)
app.secret_key = "tomibomi"

from app import data
from app import TDD
from app import authentication_views
from app import views