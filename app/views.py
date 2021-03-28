from flask import url_for, redirect, render_template, request, session

from app import app
import json

# import repositories
from app.data.repositories import UsersRepository
from app.data.repositories import DecksRepository
from app.data.repositories import CardsRepository

from app.utilities.logger import logger


@app.route("/")
def home():

    logger.info("Handling '/' route, route is called")

    if "user" in session:
        user = session["user"]

        logger.info(
            f"Handling '/' route, User {user['username']} is authenticated")
        logger.info("Handling '/' route, Rendering index.html")

        return render_template("index.html", user=user)

    logger.info("Handling '/' route, Rendering index.html")

    return render_template("index.html")


@app.route("/show_users")
def show_users():

    logger.info("Handling '/show_user' route, route is called")

    users = UsersRepository.get_all()

    logger.info("Handling '/show_user' route, rendering all users data")

    info = '<br>'.join(
        [' '.join([str(info) for info in user.get_details()]) for user in users])

    return info


@app.route("/decks")
def decks():

    logger.info("Handling '/decks' route, route is called")
    decks = DecksRepository.get_all()

    logger.info("Handling '/decks' route, rendering show_decks.html")

    return render_template("show_decks.html", decks=decks)


@app.route("/deck/<int:deck_id>")
def display_cards(deck_id: int):

    logger.info(f"Handling '/deck/{deck_id}' route, route is called")

    cards = CardsRepository.get_by_deck_id(deck_id)

    logger.info(f"Handling '/deck/{deck_id}' route, rendering show_cards.html")

    return render_template("show_cards.html", deck_id=deck_id, cards=cards)


@app.route("/deck/<int:deck_id>/card/<int:card_id>")
def card_detail(deck_id: int, card_id: int):

    logger.info(
        f"Handling '/deck/{deck_id}/card/{card_id}' route, route is called")

    card = CardsRepository.get_by_id(card_id)

    logger.info(
        "Handling '/deck/{deck_id}/card/{card_id}' route, rendering card_detail.html")
    return render_template("card_detail.html", card=card)


@app.route("/create_deck", methods=["POST", "GET"])
def create_deck():

    logger.info("Handling '/create_deck' route, route is called")

    if 'user' not in session:
        logger.info("Handling '/create_deck, user is not authenticated")
        logger.info("Handling '/create_deck, redirecting to route '/login'")
        return redirect(url_for("login"))

    username = json.loads(session['user'])['username']
    logger.info(
        f"Handling '/create_deck, user username{username} is authenticated")

    if request.method == "POST":

        name = request.form['name']
        logger.info("Handling '/create_deck, create_deck form is submitted")
        logger.info(f"Handling '/create_deck, deck name:{name}")

        user_id = json.loads(session['user'])['id']

        deck = DecksRepository.create(user_id, name)

        if deck:
            logger.info(
                "Handling '/create_deck, deck is created and saved into database")
            logger.info("Handling '/create_deck, rendering create_deck.html")
            return render_template("create_deck.html", success=True)
        else:
            logger.info(
                "Handling '/create_deck, deck is not created and is not saved into database")
            logger.info("Handling '/create_deck, rendering create_deck.html")
            return render_template("create_deck.html", success=False)

    else:
        logger.info("Handling '/create_deck, rendering create_deck.html")
        return render_template("create_deck.html")


@app.route("/deck/<int:deck_id>/create_card", methods=["GET", "POST"])
def create_card(deck_id: int):
    logger.info(
        f"Handling '/deck/{deck_id}/create_card' route, route is called")

    if 'user' not in session:
        logger.info(
            f"Handling '/deck/{deck_id}/create_card' route, user is not authenticated")
        logger.info(
            f"Handling '/deck/{deck_id}/create_card' route, redirecting to route '/login'")
        return redirect(url_for("login"))

    logger.info(
        f"Handling '/deck/{deck_id}/create_card' route, user is authenticated")
    
    if request.method == "POST":

        logger.info(
            f"Handling '/deck/{deck_id}/create_card' route, create_card form is submitted")
        word = request.form['word']
        translation = request.form["translation"]

        logger.info(
            f"Handling '/deck/{deck_id}/create_card' route, card details word: {word}, translation: {translation}")

        if CardsRepository.create(deck_id, word, translation):
            logger.info(
                f"Handling '/deck/{deck_id}/create_card' route, card is created and saved into database")
            logger.info(
                f"Handling '/deck/{deck_id}/create_card' route, rendering response")
            return "<h2>New card has been created</h2>"

        logger.info(
            f"Handling '/deck/{deck_id}/create_card' route, card has been not created")
        logger.info(
            f"Handling '/deck/{deck_id}/create_card' route, rendering response")
        return "<h2>There was some error</h2>"

    else:

        logger.info(
            f"Handling '/deck/{deck_id}/create_card' route, rendering create_card.html")
        return render_template("create_card.html")
