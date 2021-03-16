from flask import url_for, redirect, render_template, request, session

from app import app
import json

# import repositories
from app.data.repositories import UsersRepository
from app.data.repositories import DecksRepository
from app.data.repositories import CardsRepository

from app import logger

log = logger.getChild(__name__)

@app.route("/")
def home():

    log.info("route '/' is called")

    if "user" in session:
        user = session["user"]

        log.info("User is authenticated")
        log.info("Rendering index.html")

        return render_template("index.html", user=user)

    log.info("Rendering index.html")

    return render_template("index.html")
    
# TODO ADD ROLES
@app.route("/show_users")
def show_users():

    log.info("route 'show_users' is called")

    users = UsersRepository.get_all()

    log.info("Users records are retrieved from database")

    info = '<br>'.join([' '.join([str(info) for info in user.get_details()]) for user in users])

    log.info("Rendering data")

    return info


@app.route("/decks")
def decks():

    log.info("Route '/decks' is called")

    decks = DecksRepository.get_all()

    log.info("Decks records are retrieved from database")
    log.info("Rendering show_decks.html")

    return render_template("show_decks.html", decks=decks)


@app.route("/deck/<deck_id>")
def display_cards(deck_id):

    log.info("Route '/deck/<deck_id>' is called")

    cards = CardsRepository.get_by_deck_id(deck_id)

    log.info("Cards records are retrieved from database")
    log.info("Rendering show_cards.html")

    return render_template("show_cards.html", deck_id=deck_id, cards=cards)


@app.route("/deck/<deck_id>/card/<card_id>")
def card_detail(deck_id, card_id):

    log.info("Route '/deck/<deck_id>/card/<card_id>' is called")

    card = CardsRepository.get_by_id(card_id)

    log.info("Card is retrieved from database")
    log.info("Rendering card_detail.html")
    return render_template("card_detail.html", card=card)


@app.route("/create_deck", methods=["POST", "GET"])
def create_deck():

    log.info("Route '/creatE_deck' is called")

    if 'user' not in session:
        log.info("User is not authenticated")
        log.info("Redirecting to route '/login'")
        return redirect(url_for("login"))

    log.info('User is authenticated')

    if request.method == "POST":

        log.info("Form is submitted")

        name = request.form['name']

        user_id = json.loads(session['user'])['id']

        log.info("Form is processed")

        deck = DecksRepository.create(user_id, name)

        if deck:
            log.info("Deck is created and saved into database")
            log.info("Rendering create_deck.html")
            return render_template("create_deck.html", success=True)
        else:
            log.info("Deck is not created and is not saved into database")
            log.info("Rendering create_deck.html")
            return render_template("create_deck.html", success=False)

    else:
        log.info('Rendering create_deck.html')
        return render_template("create_deck.html")


@app.route("/deck/<deck_id>/create_card", methods=["GET", "POST"])
def create_card(deck_id):
    log.info("Route '/deck/<deck_id>/create_card' is called")
    
    if 'user' in session:
        log.info("User is authenticated")
        if request.method == "POST":
            
            log.info("Form is submitted")
            word = request.form['word']
            translation = request.form["translation"]

            if CardsRepository.create(deck_id, word, translation):
                log.info("Card is created and saved into database")
                log.info("Rendering response")
                return "<h2>New card has been created</h2>"
            
            log.info("Card is not created")
            log.info("Rendering response")
            return "<h2>There was some error</h2>"

        else:

            log.info("Rendering create_card.html")
            return render_template("create_card.html")

    log.info("User is not authenticated")
    log.info("Redirecting to route '/login'")
    return redirect(url_for("login"))
