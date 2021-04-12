from app import app
from app.src.utilities.logger import logger

from app.src.repositories import UsersRepository
from app.src.utilities.decorators import admin_required

@app.route("/show_users")
@admin_required
def show_users():

    logger.info("Handling '/show_users' route")

    users = UsersRepository.get_all()

    logger.info("Handling '/show_users' route, rendering all users details")

    info = '<br>'.join(
        [' '.join([str(info) for info in user.get_details()]) for user in users])

    return info
