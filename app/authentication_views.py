from flask import render_template, request, redirect, url_for
from app import app, loginManager

from app.src.utilities import crypto
from app import register_validation as validation
from app.src.repositories import UsersRepository

from app.src.utilities.logger import logger

from app.src.forms.RegistrationForm import RegistrationForm

# TODO add  generic error messages


@app.route("/register", methods=["POST", "GET"])
def register():

    logger.info("Handling '/register' route")

    if loginManager.is_authenticated():
        logger.info(
            "Handling '/register' route,  user is authenticated, redirecting to route '/home'")
        return redirect(url_for("home"))


    form = RegistrationForm(request.form)
    # TODO find a way to give information to user that email is already used.
    if request.method == "POST" and form.validate():

        logger.info(
            f"Handling '/register' route, register form is submitted. Form details username: {form.username.data}, birthday: {form.birthday.data}")

        if not UsersRepository.create(form.username.data, form.email.data, crypto.hash_password(form.password.data), form.birthday.data.strftime("%Y-%m-%d")):
            logger.error("User hasn't been created")
            return "User hasn't been created"

        logger.info(
            f"Handling '/register' route, registering new user {form.username.data} is finished successfully")
        return "success"

    logger.info(
        "Handling '/register' route, user is not authenticated and form is not submitted, rendering register.html")
    return render_template("forms/register.html", form=form)


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
