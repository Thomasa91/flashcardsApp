from flask.helpers import url_for
from werkzeug.utils import redirect
from app.data.models.Deck import Deck
from flask import render_template, request
from flask.globals import session
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
        return render_template("index.html", user = user)

    return render_template("index.html")


@app.route("/show_users")
def users():
    
    users = UsersRepository.fetchUsers()

    info = []

    for user in users:
        info.append(' '.join(str(info) for info in user.getUserDetails()))

    return '<br>'.join(info)


@app.route("/decks")
def decks():

    decks = DecksRepository.fetch_decks()

    return render_template("show_decks.html", decks = decks)


@app.route("/deck/<deck_id>")
def display_cards(deck_id):

    deck = DecksRepository.fech_deck_by_id(deck_id)

    return render_template("show_cards.html", deck = deck)


@app.route("/deck/<deck_id>/card/<card_id>")
def card_detail(deck_id, card_id):
    
    card = CardsRepository.returnCardById(card_id)

    return render_template("card_detail.html", card = card)


@app.route("/create_deck", methods=["POST", "GET"])
def create_deck():

    if not 'user' in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        name = request.form['name']

        user_id = json.loads(session['user'])['id']

        deck = DecksRepository.createDeck(user_id, name)

        if DecksRepository.saveToDataBase(deck):
            return render_template("create_deck.html", success=True)
        else:
            return render_template("create_deck.html", success=False)

    else:
        return render_template("create_deck.html")

@app.route("/deck/<id>/create_card", methods=["GET", "POST"])
def create_card(id):

    if not 'user' in session:
        return redirect(url_for("login"))


    if request.method == "POST":

        word = request.form['word']
        translation = request.form["translation"]
        
        card = CardsRepository.createCard(id, word, translation)

        
        if CardsRepository.saveCardToDataBase(card):
            return "<h2>Error occured</h2>"
    
        return "<h2>gz</h2>"

    else:
        return render_template("create_card.html")
