from flask import render_template, request

from app import app, loginManager

from app.src.repositories import DecksRepository
from app.src.repositories import CardsRepository

from app.src.utilities.logger import logger

from app.src.utilities.decorators import login_required


@app.route("/")
def home():

    logger.info("Handling '/' route")

    if loginManager.is_authenticated():
        user = loginManager.get_username()

        logger.info(
            f"Handling '/' route, User {user} is authenticated")
        logger.info("Handling '/' route, rendering index.html")

        return render_template("index.html", user=user)

    logger.info(
        "Handling '/' route, user is not authenticated, rendering index.html")

    return render_template("index.html")


@app.route("/decks")
@login_required
def decks():

    logger.info("Handling '/decks' route")
    user_id = loginManager.get_id()

    decks = DecksRepository.get_by_user_id(user_id)

    logger.info("Handling '/decks' route, rendering show_decks.html")
    return render_template("show_decks.html", decks=decks)


@app.route("/deck/<int:deck_id>")
@login_required
def display_cards(deck_id: int):

    logger.info(f"Handling '/deck/{deck_id}' route")

    cards = CardsRepository.get_by_deck_id(deck_id)

    logger.info(f"Handling '/deck/{deck_id}' route, rendering show_cards.html")

    return render_template("show_cards.html", deck_id=deck_id, cards=cards)


@app.route("/deck/<int:deck_id>/card/<int:card_id>")
@login_required
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
@login_required
def create_deck():

    logger.info("Handling '/create_deck' route")

    if request.method == "POST":

        name = request.form['name']
        logger.info(
            f"Handling '/create_deck, create_deck form is submitted. Form details deck_name:{name}")

        user_id = loginManager.get_id()

        if DecksRepository.create(user_id, name):
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
@login_required
def create_card(deck_id: int):
    logger.info(
        f"Handling '/deck/{deck_id}/create_card' route")

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

            return "<h2>Card has been not created</h2>"

        logger.info(
            f"Handling '/deck/{deck_id}/create_card' route, card is created")
        logger.info(
            f"Handling '/deck/{deck_id}/create_card' route, rendering response")

        return "<h2>New card has been created</h2>"

    logger.info(
        f"Handling '/deck/{deck_id}/create_card' route, rendering create_card.html")
    return render_template("create_card.html")
