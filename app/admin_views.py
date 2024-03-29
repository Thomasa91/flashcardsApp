from app import app
from app.src.utilities.logger import logger

from app.src.repositories import UsersRepository


@app.route("/users")
def show_users():

    logger.info("Handling '/users' route")

    users = UsersRepository.get_all()

    logger.info("Handling '/users' route, rendering all users details")

    info = '<br>'.join(
        [' '.join([str(info) for info in user.get_details()]) for user in users])

    return info
