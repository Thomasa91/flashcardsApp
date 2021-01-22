from flask import render_template, request
from app import app
from app import database_context

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/decks")
def decks():
    conn = database_context.connect()

    cursor = conn.cursor()

    query = "SELECT * FROM deck;"

    cursor.execute(query)

    results = cursor.fetchall()

    return render_template("show_decks.html", decks = results)
# TODO deck/id/cards
@app.route("/deck/<deck_id>")
def display_cards(deck_id):

    conn= database_context.connect()

    cursor = conn.cursor()

    querry = f"SELECT * FROM card WHERE deck_id == {deck_id};"

    cursor.execute(querry)

    cards = cursor.fetchall()

    return render_template("show_cards.html", cards = cards, deck_id = deck_id)

@app.route("/deck/<deck_id>/card/<card_id>")
def card_detail(deck_id, card_id):
    
    conn = database_context.connect()

    cursor = conn.cursor()

    querry = f"SELECT word, translation FROM card WHERE deck_id == {deck_id} AND card_id == {card_id};"

    cursor.execute(querry)

    card = cursor.fetchone()
    
    word = card[0]
    translation = card[1]

    return render_template("card_detail.html", word = word, translation = translation)

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


@app.route("/deck/<id>/create_card", methods=["GET", "POST"])
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
        return render_template("create_card.html")
