from flask import Flask

app = Flask(__name__)

from app import authentication_views
from app import views