from flask import render_template, request, session, redirect, url_for
from app import app

from app.utilities import crypto
from app import register_validation as validation
from app.data.repositories import UsersRepository

from app import logger

log = logger.getChild(__name__)

# TODO add  generic error messages
@app.route("/register", methods=["POST", "GET"])
def register():
    
    log.info("Route /register is called")
    if "user" in session:
        log.info("User is authenticated")
        log.info("Redirecting to route 'home'")
        return redirect(url_for("home"))

    elif request.method == "POST":
        log.info("Form is submitted")

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        birthday = request.form['birthday']


        if not validation.validate_date_format(birthday):
            return "wrong date format"

        if UsersRepository.get_by_username_email(username, email):
            return "User already exits"

        if not validation.validate_password(password):
            return "at least 1 capital letter, 1 small letter, 1 number, length 8 - 20"

        if not validation.validate_email(email):
            return "wrong email format"

        if UsersRepository.create(username, email, crypto.hash_password(password), birthday):
            return "success"

        return "Something went wrong"

    else:
        log.info("Rendering register.html")
        return render_template("forms/register.html")


@app.route("/login", methods=["POST", "GET"])
def login():

    log.info("Route '/login' is called")
    if "user" in session:
        log.info("User is authenticated")
        log.info("Redirecting to route '/home'")
        return redirect(url_for("home"))

    elif request.method == "POST":
        log.info("Form is submitted")
        username = request.form['username']
        password = request.form['password'] 
        log.info("Form is processed")
        user = UsersRepository.get_by_name(username)

        if user:
            logger.info(' '.join(user.get_details))
            if user.password == crypto.hash_password(password):
                log.info("User is authenticated")
                session["user"] = user.to_json()
                log.info("Redirecting to route 'home'")
                return redirect(url_for("home"))

        log.info("User is not authenticated")
        return "something went wrong"

    else:
        log.info("Rendering login.html")
        return render_template("forms/login.html")
