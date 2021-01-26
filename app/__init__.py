from flask import Flask, session

app = Flask(__name__)
app.secret_key = "tomibomi"

from app import views
from app import authentication_views