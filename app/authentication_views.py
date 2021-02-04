from flask import render_template, request, session, redirect
from flask.helpers import url_for

from app import app
from app.data.repositories import UsersRepository


@app.route("/register", methods=["POST", "GET"])
def register():

    if "user" in session:
        return redirect(url_for("home"))

    elif request.method == "POST":

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # TODO add validation and change format
        birthday = request.form['birthDay'].split("-")[0]


        user = UsersRepository.create(username, email, password, birthday)

        # TODO change responses later/save user by using UsersRepository
        if user.ifExists():
            return "User already exits"
        if not user.validatePassword():
            return "at least 1 capital letter, 1 small letter, 1 number, length 8 - 20"

        if not user.validateEmail():
            return "email has wrong format"

        if UsersRepository.save(user):
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

        user = UsersRepository.getByName(username)

        if user:

            if user.password == password:

                session["user"] = user.to_json()

                return redirect(url_for("home"))

        return "something went wrong"

    else:
     return render_template("forms/login.html")