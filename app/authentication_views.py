from flask import render_template, request, session, redirect
from flask.helpers import url_for
from app import app, database_context



@app.route("/register", methods=["POST" ,"GET"])
def register():


    if "user" in session:
        return redirect("home")

    elif request.method == "POST":

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        birthDay = request.form['birthDay'].split("-")[0]


        conn = database_context.connect()

        c = conn.cursor()

        # check if user exists
        query = "SELECT user_name FROM user WHERE user_name = '{username}' OR user_email = '{email}'"

        c.execute(query)

        user = c.fetchone()
        
        if user:
            return "User already exits"
        else:

            query = f"INSERT INTO user (user_name, user_email, user_password, date_of_birth) VALUES ('{username}', '{email}', '{password}', '{birthDay}');"

            c.execute(query)

            conn.commit()

            if c.lastrowid:
                return "Bravo"
            else:
                return "something went wrong"

    else:
        return render_template("forms/register.html")


@app.route("/login", methods=["POST", "GET"])
def login():

    if "user" in session:
        return redirect(url_for("home"))

    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password'] 

        conn = database_context.connect()

        c = conn.cursor()

        query = f"SELECT user_id, user_name FROM user WHERE user_name = '{username}' AND user_password = '{password}';"

        c.execute(query)

        user = c.fetchone()

        if user:
            session["user"] = user[1]

            return redirect(url_for("home"))
        else:
            return f"something went wrong {user}"

    else:
     return render_template("forms/login.html")