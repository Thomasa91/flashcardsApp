from flask import render_template, request, redirect, url_for
from app import app

from app.src.repositories import UsersRepository

from app.src.utilities.logger import logger
from app.src.utilities.crypto import hash_password, check_password_hash

from app.src.forms.RegistrationForm import RegistrationForm
from app.src.forms.LoginForm import LoginForm

from flask_login import current_user, logout_user, login_user, login_required
# TODO add  generic error messages


@app.route("/register", methods=["POST", "GET"])
def register():

    logger.info("Handling '/register' route")

    if current_user.is_authenticated:
        logger.info(
            "Handling '/register' route,  user is authenticated, redirecting to route '/home'")
        return redirect(url_for("home"))

    form = RegistrationForm(request.form)
    
    if request.method == "POST" and form.validate():

        logger.info(
            f"Handling '/register' route, register form is submitted. Form details username: {form.username.data}, birthday: {form.birthday.data}")

        if not UsersRepository.create(form.username.data, form.email.data, hash_password(form.password.data), form.birthday.data.strftime("%Y-%m-%d")):
            logger.error("User has not been created")
            return "User has not been created"

        logger.info(
            f"Handling '/register' route, registering new user {form.username.data} is finished successfully")
        return "success"

    logger.info(
        "Handling '/register' route, user is not authenticated and form is not submitted, rendering register.html")
    return render_template("forms/register.html", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():

    logger.info("Handling '/login' route")
    if current_user.is_authenticated:
        logger.info(
            "Handling '/login' route,  user is authenticated, redirecting to route '/home'")
        return redirect(url_for("home"))

    form = LoginForm(request.form)

    if request.method == "POST" and form.validate():

        username = form.username.data
        password = form.password.data

        logger.info(
            f"Handling '/login' route, login form is submitted. Form details username field: {username}")

        user = UsersRepository.get_by_username(username)

        if user:
            if check_password_hash(user.password, password):

                logger.info(
                    "Handling '/login' route, authenticating user {username} finished successfully")
                
                login_user(user)

                logger.info(
                    "Handling '/login' route, user is authenticated, redirecting to route 'home'")
                return redirect(url_for("home"))

        logger.error(
            f"Handling '/login' route, authenticating user {username} failed")
        form.password.errors.append("Username or password is invalid")
    
    logger.info(
        "Handling '/login' route, user is not authenticated, rendering login.html")
    return render_template("forms/login.html", form=form)

@login_required
@app.route("/logout")
def logout():
    name = current_user.username
    logout_user()
    logger.info(f"User {name} has been logout from the session")
    return redirect(url_for("home"))
