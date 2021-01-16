from app import app
from app import database_context

from flask import render_template, request


@app.route("/create_deck", methods=["POST", "GET"])
def create_deck():

    
    if request.method == "POST":
        name = request.form['name']

        conn = database_context.connect()

        sql_query = f"INSERT INTO deck (name) VALUES('{name}');"

        cursor = conn.cursor()

        cursor.execute(sql_query)

        conn.commit()

        if cursor.rowcount == 1:
            return render_template("create_deck.html", success=True)
        else:
            return render_template("create_deck.html", success=False)
    else:
        return render_template("create_deck.html")


@app.route("/<id>/cards/create_card", methods=["GET", "POST"])
def create_card(id):

    if request.method == "POST":

        word = request.form['word']
        translation = request.form["translation"]

        conn = database_context.connect()

        sql_query = f"INSERT INTO card (deck_id, word, translation) VALUES ({id}, '{word}', '{translation}');"

        cursor = conn.cursor()

        cursor.execute(sql_query)

        conn.commit()

        if cursor.rowcount < 1:
            return "<h2>Error occured</h2>"
    

        return "<h2>gz</h2>"

    else:

        return render_template("new_card.html")
