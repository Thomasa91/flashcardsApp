from flask_login import LoginManager
from app import app
from app.src.models.User import User
from app.src.repositories import UsersRepository

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id) -> User:
    return UsersRepository.get_by_id(user_id)
