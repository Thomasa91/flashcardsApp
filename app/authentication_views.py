from flask import render_template, request, redirect, url_for
from app import app

from app.src.utilities import crypto
from app import register_validation as validation
from app.src.repositories import UsersRepository

from app.src.utilities.logger import logger
from app.src.utilities import loginManager

# TODO add  generic error messages


@app.route("/register", methods=["POST", "GET"])
def register():

    logger.info("Handling '/register' route")

    if loginManager.is_authenticated():
        logger.info(
            "Handling '/register' route,  user is authenticated, redirecting to route '/home'")
        return redirect(url_for("home"))

    if request.method == "POST":

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        birthday = request.form['birthday']


        logger.info(
            f"Handling '/register' route, register form is submitted. Form details username: {username}, birthday: {birthday}")

        if not validation.validate_date_format(birthday):
            logger.error(
                f"Handling '/register' route, registering new user {username} failed: invalid date format")
            return "wrong date format"

        # TODO tell if email or username is taken
        if UsersRepository.get_by_username_email(username, email):
            logger.error(
                f"Handling '/register' route, registering new user {username} failed: User already exits")
            return "User already exits"

        # TODO return more detailed information
        if not validation.validate_password(password):
            logger.error(
                f"Handling '/register' route, registering new user {username} failed: invalid password")
            return "at least 1 capital letter, 1 small letter, 1 number, length 8 - 20"

        if not validation.validate_email(email):
            logger.error(
                f"Handling '/register' route, registering new user {username} failed: invalid email format")
            return "wrong email format"

        if not UsersRepository.create(username, email, crypto.hash_password(password), birthday):
            return "User has been not created"

        logger.info(
            f"Handling '/register' route, registering new user {username} is finished successfully")
        return "success"

    logger.info(
        "Handling '/register' route, user is not authenticated and form is not submitted, rendering register.html")
    return render_template("forms/register.html")


@app.route("/login", methods=["POST", "GET"])
def login():

    logger.info("Handling '/login' route")
    if loginManager.is_authenticated():
        logger.info(
            "Handling '/login' route,  user is authenticated, redirecting to route '/home'")
        return redirect(url_for("home"))

    if request.method == "POST":

        username = request.form['username']
        password = request.form['password']
        
        logger.info(
            f"Handling '/login' route, login form is submitted. Form details username field: {username}")

        # TODO Find a way to show user if password or username was invalid
        if not loginManager.authenticate(username, password):
            logger.error(f"Handling '/login' route, authenticating user {username} failed")
            return "invalid username or password"

        logger.info("Handling '/login' route, authenticating user {username} finished successfully")
        logger.info(
            "Handling '/login' route, user is authenticated, redirecting to route 'home'")
        return redirect(url_for("home"))

        
    logger.info(
        "Handling '/login' route, user is not authenticated, rendering login.html")
    return render_template("forms/login.html")
