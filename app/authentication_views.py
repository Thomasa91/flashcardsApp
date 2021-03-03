from flask import render_template, request, session, redirect, url_for
from app import app

from app.utilities import crypto
from app import register_validation as validation
from app.data.repositories import UsersRepository


# TODO add  generic error messages
@app.route("/register", methods=["POST", "GET"])
def register():

    if "user" in session:
        return redirect(url_for("home"))

    elif request.method == "POST":

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        birthday = request.form['birthday']

        # TODO change return statements
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
        return render_template("forms/register.html")


@app.route("/login", methods=["POST", "GET"])
def login():

    if "user" in session:
        return redirect(url_for("home"))

    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password'] 

        user = UsersRepository.get_by_name(username)

        if user:

            if user.password == crypto.hash_password(password):

                session["user"] = user.to_json()

                return redirect(url_for("home"))

        return "something went wrong"

    else:
        return render_template("forms/login.html")
