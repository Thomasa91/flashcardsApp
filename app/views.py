from flask import url_for, redirect, render_template, request, session

from app import app
import json

# import repositories
from app.src.repositories import UsersRepository
from app.src.repositories import DecksRepository
from app.src.repositories import CardsRepository

from app.utilities.logger import logger


@app.route("/")
def home():

    logger.info("Handling '/' route")

    if "user" in session:
        user = session["user"]

        logger.info(
            f"Handling '/' route, User {user['username']} is authenticated")
        logger.info("Handling '/' route, Rendering index.html")

        return render_template("index.html", user=user)

    logger.info(
        "Handling '/' route, user is not authenticated Rendering index.html")

    return render_template("index.html")


@app.route("/show_users")
def show_users():

    logger.info("Handling '/show_user' route")

    users = UsersRepository.get_all()

    logger.info("Handling '/show_user' route, rendering all users src")

    info = '<br>'.join(
        [' '.join([str(info) for info in user.get_details()]) for user in users])

    return info


@app.route("/decks")
def decks():

    logger.info("Handling '/decks' route")
    decks = DecksRepository.get_all()

    logger.info("Handling '/decks' route, rendering show_decks.html")

    return render_template("show_decks.html", decks=decks)


@app.route("/deck/<int:deck_id>")
def display_cards(deck_id: int):

    logger.info(f"Handling '/deck/{deck_id}' route")

    cards = CardsRepository.get_by_deck_id(deck_id)

    logger.info(f"Handling '/deck/{deck_id}' route, rendering show_cards.html")

    return render_template("show_cards.html", deck_id=deck_id, cards=cards)


@app.route("/deck/<int:deck_id>/card/<int:card_id>")
def card_detail(deck_id: int, card_id: int):

    logger.info(
        f"Handling '/deck/{deck_id}/card/{card_id}' route")

    card = CardsRepository.get_by_id(card_id)

    if not card:
        logger.error(
            f"Handling '/deck/{deck_id}/card/{card_id}' route, card with id: {card_id} doesn't exist")
        return "Card doesn't exist"

    logger.info(
        "Handling '/deck/{deck_id}/card/{card_id}' route, rendering card_detail.html")
    return render_template("card_detail.html", card=card)


@app.route("/create_deck", methods=["POST", "GET"])
def create_deck():

    logger.info("Handling '/create_deck' route")

    if 'user' not in session:
        logger.info("Handling '/create_deck, user is not authenticated")
        logger.info("Handling '/create_deck, redirecting to route '/login'")
        return redirect(url_for("login"))

    username = json.loads(session['user'])['username']
    logger.info(
        f"Handling '/create_deck, user {username} is authenticated")

    if request.method == "POST":

        name = request.form['name']
        logger.info(
            f"Handling '/create_deck, create_deck form is submitted. Form details deck_name:{name}")

        user_id = json.loads(session['user'])['id']

        deck = DecksRepository.create(user_id, name)

        if deck:
            logger.info(
                "Handling '/create_deck, deck is created")
            logger.info("Handling '/create_deck, rendering create_deck.html")
            return render_template("create_deck.html", success=True)

        logger.error(
            "Handling '/create_deck, deck is not created")
        logger.info("Handling '/create_deck, rendering create_deck.html")
        return render_template("create_deck.html", success=False)

    logger.info("Handling '/create_deck, rendering create_deck.html")
    return render_template("create_deck.html")


@app.route("/deck/<int:deck_id>/create_card", methods=["GET", "POST"])
def create_card(deck_id: int):
    logger.info(
        f"Handling '/deck/{deck_id}/create_card' route")

    if 'user' not in session:
        logger.info(
            f"Handling '/deck/{deck_id}/create_card' route, user is not authenticated")
        logger.info(
            f"Handling '/deck/{deck_id}/create_card' route, redirecting to route '/login'")
        return redirect(url_for("login"))

    logger.info(
        f"Handling '/deck/{deck_id}/create_card' route, user is authenticated")

    if request.method == "POST":

        word = request.form['word']
        translation = request.form["translation"]

        logger.info(
            f"Handling '/deck/{deck_id}/create_card' route, create_card form is submitted. Form details word: {word}, translation: {translation}")

        if not CardsRepository.create(deck_id, word, translation):
            logger.error(
                f"Handling '/deck/{deck_id}/create_card' route, card has been not created")
            logger.info(
                f"Handling '/deck/{deck_id}/create_card' route, rendering response")

            return "<h2>There was some error</h2>"

        logger.info(
            f"Handling '/deck/{deck_id}/create_card' route, card is createde")
        logger.info(
            f"Handling '/deck/{deck_id}/create_card' route, rendering response")

        return "<h2>New card has been created</h2>"

    logger.info(
        f"Handling '/deck/{deck_id}/create_card' route, user is authenticated. Rendering create_card.html")
    return render_template("create_card.html")
