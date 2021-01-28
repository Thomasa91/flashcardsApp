from flask import render_template, request, session, redirect
from flask.helpers import url_for

from app import app
from app.data.models import User
from app.data.repositories import UsersRepository


@app.route("/register", methods=["POST", "GET"])
def register():

    if "user" in session:
        return redirect(url_for("home"))

    elif request.method == "POST":

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        birthDay = request.form['birthDay'].split("-")[0]


        user = User(username, email, password, birthDay)

        # TODO change responses later
        if user.ifUserExists():
            return "User already exits"
        if not user.validatePassword():
            return "at least 1 capital letter, 1 small letter, 1 number, length 8 - 20"

        if not user.validateEmail():
            return "email has wrong format"

        if user.saveUserToDataBase():
            return "success"

        return "Something went wrong"

    else:
        return render_template("forms/register")


@app.route("/login", methods=["POST", "GET"])
def login():

    if "user" in session:
        return redirect(url_for("home"))

    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password'] 

        user = UsersRepository.fetchUserByName(username)

        if user:

            if user.password == password:

                session["user"] = user

                return redirect(url_for("home"))

        return f"something went wrong"

    else:
     return render_template("forms/login.html")