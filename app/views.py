from flask import url_for, redirect, render_template, request, session

from app import app
import json

# import repositories
from app.data.repositories import UsersRepository
from app.data.repositories import DecksRepository
from app.data.repositories import CardsRepository


@app.route("/")
def home():
    if "user" in session:
        user = session["user"]
        return render_template("index.html", user=user)

    return render_template("index.html")


# TODO ADD ROLES
@app.route("/show_users")
def show_users():
    users = UsersRepository.get_all()

    info = '<br>'.join([' '.join([str(info) for info in user.get_details()]) for user in users])

    return info


@app.route("/decks")
def decks():
    decks = DecksRepository.get_all()

    return render_template("show_decks.html", decks=decks)


@app.route("/deck/<deck_id>")
def display_cards(deck_id):
    cards = CardsRepository.get_by_deck_id(deck_id)

    return render_template("show_cards.html", deck_id=deck_id, cards=cards)


@app.route("/deck/<deck_id>/card/<card_id>")
def card_detail(deck_id, card_id):
    card = CardsRepository.get_by_id(card_id)

    return render_template("card_detail.html", card=card)


@app.route("/create_deck", methods=["POST", "GET"])
def create_deck():
    if 'user' not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        name = request.form['name']

        user_id = json.loads(session['user'])['id']

        deck = DecksRepository.create(user_id, name)

        if deck:
            return render_template("create_deck.html", success=True)
        else:
            return render_template("create_deck.html", success=False)

    else:
        return render_template("create_deck.html")


@app.route("/deck/<id>/create_card", methods=["GET", "POST"])
def create_card(card_id):
    if 'user' in session:

        if request.method == "POST":

            word = request.form['word']
            translation = request.form["translation"]

            if CardsRepository.create(card_id, word, translation):
                return "<h2>gz</h2>"

            return "<h2>error</h2>"

        else:
            return render_template("create_card.html")

    return redirect(url_for("login"))
