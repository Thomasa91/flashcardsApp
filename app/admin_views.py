from app import app
from app.src.utilities.logger import logger

from app.src.repositories import UsersRepository

@app.route("/show_users")
def show_users():

    logger.info("Handling '/show_user' route")

    users = UsersRepository.get_all()

    logger.info("Handling '/show_user' route, rendering all users src")

    info = '<br>'.join(
        [' '.join([str(info) for info in user.get_details()]) for user in users])

    return info