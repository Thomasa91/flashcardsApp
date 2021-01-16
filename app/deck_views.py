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
