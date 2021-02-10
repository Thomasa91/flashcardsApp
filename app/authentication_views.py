from flask import render_template, request, session, redirect
from flask.helpers import url_for

import re

from app import app
from app.data.repositories import UsersRepository

#TODO  Maybe later try to use cyptography library, using key to hash password ?
# https://www.mssqltips.com/sqlservertip/5173/encrypting-passwords-for-use-with-python-and-sql-server/


from hashlib import sha256

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

        
            if user.password == hash_password(password):

                session["user"] = user.to_json()

                return redirect(url_for("home"))

        return "something went wrong"

    else:
     return render_template("forms/login.html")

#TODO WHERE I SHOULD HASH PASSWORD. USER CLASS ?
#TODO WHERE TO PUT THOSE METHODS
def hash_password(password):
    h = sha256()

    h.update(password)

    return h.hexdigest().encode('utf-8')

def check_date_format(date):

    pattern = r"^\d{4}-\d{2}-\d{2}$"

    return re.match(pattern, date)

