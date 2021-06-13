from flask import Flask
from flask_login import LoginManager
from app.src.repositories import UsersRepository

app = Flask(__name__)
app.secret_key = 'Tomibomi'


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return UsersRepository.get_by_id(user_id)


from app import authentication_views
from app import views
from app import admin_views