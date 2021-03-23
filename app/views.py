from flask import url_for, redirect, render_template, request, session

from app import app
import json

# import repositories
from app.data.repositories import UsersRepository
from app.data.repositories import DecksRepository
from app.data.repositories import CardsRepository

from app.logs.logger import logger


@app.route("/")
def home():

    logger.info("Home page, route '/' is called")

    if "user" in session:
        user = session["user"]

        logger.info(f"Home page, User {user['username']} is authenticated")
        logger.info("Home page, Rendering index.html")

        return render_template("index.html", user=user)

    logger.info("Home page, Rendering index.html")

    return render_template("index.html")

# TODO ADD ROLES


@app.route("/show_users")
def show_users():

    logger.info("Showing users, route '/show_users' is called")

    users = UsersRepository.get_all()

    logger.info("Showing users, rendering all users data")

    info = '<br>'.join(
        [' '.join([str(info) for info in user.get_details()]) for user in users])

    return info


@app.route("/decks")
def decks():

    logger.info("Showing decks, route '/decks' is called")
    decks = DecksRepository.get_all()

    logger.info("Showing decks, rendering show_decks.html")

    return render_template("show_decks.html", decks=decks)


@app.route("/deck/<deck_id>")
def display_cards(deck_id):

    logger.info(f"Showing cards, route '/deck/{deck_id}' is called")

    cards = CardsRepository.get_by_deck_id(deck_id)

    logger.info("Showing cards, rendering show_cards.html")

    return render_template("show_cards.html", deck_id=deck_id, cards=cards)


@app.route("/deck/<deck_id>/card/<card_id>")
def card_detail(deck_id, card_id):

    logger.info(
        f"Showing card detail, route '/deck/{deck_id}/card/{card_id}' is called")

    card = CardsRepository.get_by_id(card_id)

    logger.info("Showing card detail, rendering card_detail.html")
    return render_template("card_detail.html", card=card)


@app.route("/create_deck", methods=["POST", "GET"])
def create_deck():

    logger.info("Creating new deck,route '/create_deck' is called")

    if 'user' not in session:
        logger.info("Creating new deck, user is not authenticated")
        logger.info("Creating new deck, redirecting to route '/login'")
        return redirect(url_for("login"))

    username = json.loads(session['user'])['username']
    logger.info(f'Creating new deck, user username{username} is authenticated')

    if request.method == "POST":

        name = request.form['name']
        logger.info("Creating new deck, create_deck form is submitted")
        logger.info(f"Creating new deck, deck name:{name}")

        user_id = json.loads(session['user'])['id']

        deck = DecksRepository.create(user_id, name)

        if deck:
            logger.info(
                "Creating new deck, deck is created and saved into database")
            logger.info("Creating new deck, rendering create_deck.html")
            return render_template("create_deck.html", success=True)
        else:
            logger.info(
                "Creating new deck, deck is not created and is not saved into database")
            logger.info("Creating new deck, rendering create_deck.html")
            return render_template("create_deck.html", success=False)

    else:
        logger.info('Creating new deck, rendering create_deck.html')
        return render_template("create_deck.html")


@app.route("/deck/<deck_id>/create_card", methods=["GET", "POST"])
def create_card(deck_id):
    logger.info(
        f"Creating new card, route '/deck/{deck_id}/create_card' is called")

    if 'user' in session:
        logger.info("Creating new card, user is authenticated")
        if request.method == "POST":

            logger.info("Creating new card, form is submitted")
            word = request.form['word']
            translation = request.form["translation"]

            logger.info(
                f"Creating new card, word: {word}, translation: {translation}")

            if CardsRepository.create(deck_id, word, translation):
                logger.info(
                    "Creating new card, card is created and saved into database")
                logger.info("Creating new card, rendering response")
                return "<h2>New card has been created</h2>"

            logger.info("Creating new card, card has been not created")
            logger.info("Creating new card, rendering response")
            return "<h2>There was some error</h2>"

        else:

            logger.info("Creating new card, rendering create_card.html")
            return render_template("create_card.html")

    logger.info("Creating new card, user is not authenticated")
    logger.info("Creating new card, redirecting to route '/login'")
    return redirect(url_for("login"))
