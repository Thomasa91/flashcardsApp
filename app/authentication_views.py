from flask import render_template, request, session, redirect
from flask.helpers import url_for

import re

from app import app
#TODO should this file be in APP folder or out of it like now ?
from help import crypto
from app.data.repositories import UsersRepository


@app.route("/register", methods=["POST", "GET"])
def register():

    if "user" in session:
        return redirect(url_for("home"))

    elif request.method == "POST":

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        birthday = request.form['birthDay']

        if not check_date_format(birthday):
            return "something wrong"


        # TODO change responses later/save user by using UsersRepositor
        if UsersRepository.getByEmailUsername(username, email):
            return "User already exits"
        #TODO still don't know where i should put those methods, maybe create form classes that will generate form, get data from it and put validation method there? I've seen something like this in frameworks. If it would be good exercise then I can do this :)
        if not user.validatePassword():
            return "at least 1 capital letter, 1 small letter, 1 number, length 8 - 20"

        if not user.validateEmail():
            return "email has wrong format"

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

        user = UsersRepository.getByName(username)

        if user:

            if user.password == crypto.hash_password(password):

                # TODO how to store user in session now I use method to_json in user. is it okey or should do this in another way?
                session["user"] = user.to_json()

                return redirect(url_for("home"))

        return "something went wrong"

    else:
     return render_template("forms/login.html")


# TODO where to move this shit
def check_date_format(date):

    pattern = r"^\d{4}-\d{2}-\d{2}$"

    return re.match(pattern, date)

