from flask import render_template, request, session, redirect, url_for
from app import app

from app.utilities import crypto
from app import register_validation as validation
from app.data.repositories import UsersRepository

from app.utilities.logger import logger


# TODO add  generic error messages
@app.route("/register", methods=["POST", "GET"])
def register():

    logger.info("Handling '/register' route, route /register is called")
    if "user" in session:
        logger.info("Handling '/register' route, user is authenticated")
        logger.info("Handling '/register' route, redirecting to route 'home'")
        return redirect(url_for("home"))

    elif request.method == "POST":
        logger.info("Handling '/register' route, register form is submitted")

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        birthday = request.form['birthday']

        logger.info(
            f"Handling '/register' route, Form details username: {username}, email: {email}, password: {password}, birthday: {birthday}")

        if not validation.validate_date_format(birthday):
            logger.error(
                f"Handling '/register' route, registering new user {username} failed: invalid date format")
            return "wrong date format"

        if UsersRepository.get_by_username_email(username, email):
            logger.error(
                f"Handling '/register' route, registering new user {username} failed: User already exits")
            return "User already exits"

        if not validation.validate_password(password):
            logger.error(
                f"Handling '/register' route, registering new user {username} failed: invalid password")
            return "at least 1 capital letter, 1 small letter, 1 number, length 8 - 20"

        if not validation.validate_email(email):
            logger.error(
                f"Handling '/register' route, registering new user {username} failed: invalid email format")
            return "wrong email format"

        if UsersRepository.create(username, email, crypto.hash_password(password), birthday):
            logger.info(
                f"Handling '/register' route, registering new user {username} is finished")
            return "success"

        logger.error(
            f"Handling '/register' route, registering new user {username} failed")
        return "Something went wrong"

    else:
        logger.info("Handling '/register' route, rendering register.html")
        return render_template("forms/register.html")


@app.route("/login", methods=["POST", "GET"])
def login():

    logger.info("Handling '/login' route, route '/login' is called")
    if "user" in session:
        logger.info("Handling '/login' route, user is authenticated")
        logger.info("Handling '/login' route, redirecting to route '/home'")
        return redirect(url_for("home"))

    elif request.method == "POST":

        logger.info("Handling '/login' route, login form is submitted")
        username = request.form['username']
        password = request.form['password']
        user = UsersRepository.get_by_name(username)
        logger.info(
            f"Handling '/login' route, Form details username field: {username}, password field:{password}")

        if user:
            logger.info(
                f"Handling '/login' route, authenticating user {user.username}")
            if user.password == crypto.hash_password(password):
                session["user"] = user.to_json()
                logger.info(
                    f"Handling '/login' route, authenticating user {user.username} finished successfully")
                logger.info(
                    "Handling '/login' route, redirecting to route 'home'")
                return redirect(url_for("home"))

        logger.error(
            f"Handling '/login' route, authenticating user {user.username} failed: Invalid username or password")
        logger.info("Handling '/login' route, redirecting to '/home' route")
        return "something went wrong"

    else:
        logger.info("Handling '/login' route, rendering login.html")
        return render_template("forms/login.html")
