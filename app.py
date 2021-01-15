from flask import Flask, render_template
import database_context

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/decks")
def display_decks():
    conn = database_context.connect()

    # GET ALL DECKS

    cursor = conn.cursor()

    query = "SELECT * FROM deck;"

    cursor.execute(query)

    results = cursor.fetchall()

    return render_template("show_decks.html", decks = results)

@app.route("/<id>/cards")
def display_cards(id):

    conn= database_context.connect()

    cursor = conn.cursor()

    querry = f"SELECT * FROM card WHERE deck_id == {id};"

    cursor.execute(querry)

    cards = cursor.fetchall()

    return render_template("show_cards.html", cards = cards)

if __name__ == "__main__":
    app.run(debug=True)

