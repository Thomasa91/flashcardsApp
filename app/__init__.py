from flask import Flask

app = Flask(__name__)
app.secret_key = 'Tomibomi'

from app import authentication_views
from app import views