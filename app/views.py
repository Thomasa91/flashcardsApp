from flask import render_template, request, redirect
from flask.helpers import url_for

from app import app

from app.src.repositories import DecksRepository
from app.src.repositories import CardsRepository

from app.src.utilities.logger import logger

from app.src.forms.CardForm import CardForm
from app.src.forms.DeckForm import DeckForm

from flask_login import login_required, current_user

@app.route("/")
def home():

    logger.info("Handling '/' route")

    if current_user.is_authenticated:
        user = current_user.username

        logger.info(
            f"Handling '/' route, User {user} is authenticated")
        logger.info("Handling '/' route, rendering index.html")

        return render_template("index.html", user=user)

    logger.info(
        "Handling '/' route, user is not authenticated, rendering index.html")

    return render_template("index.html")


@app.route("/decks/view")
@login_required
def decks():

    logger.info("Handling '/decks/view' route")
    user_id = current_user.get_id()

    decks = DecksRepository.get_by_user_id(user_id)

    logger.info("Handling '/decks/view' route, rendering show_decks.html")
    return render_template("show_decks.html", decks=decks)


@app.route("/decks/<int:deck_id>/cards/view")
@login_required
def display_cards(deck_id: int):

    logger.info(f"Handling '/decks/{deck_id}/cards/view' route")

    cards = CardsRepository.get_by_deck_id(deck_id)

    logger.info(f"Handling '/decks/{deck_id}/cards/view' route, rendering show_cards.html")

    return render_template("show_cards.html", deck_id=deck_id, cards=cards)


@app.route("/decks/<int:deck_id>/cards/<int:card_id>/view")
@login_required
def card_detail(deck_id: int, card_id: int):

    logger.info(
        f"Handling '/decks/{deck_id}/cards/{card_id}/view' route")

    card = CardsRepository.get_by_id(card_id)

    if not card:
        logger.error(
            f"Handling '/decks/{deck_id}/cards/{card_id}/view' route, card with id: {card_id} doesn't exist")
        return "Card doesn't exist"

    logger.info(
        f"Handling '/decks/{deck_id}/cards/{card_id}/view' route, rendering card_detail.html")
    return render_template("card_detail.html", card=card)


@app.route("/decks/create", methods=["POST", "GET"])
@login_required
def create_deck():

    logger.info("Handling 'decks/create' route")

    form = DeckForm(request.form)

    if request.method == "POST" and form.validate():

        name = form.name.data

        logger.info(
            f"Handling 'decks/create, create_deck form is submitted. Form details deck_name:{name}")

        user_id = current_user.get_id()

        if DecksRepository.create(user_id, name):
            logger.info(
                "Handling 'decks/create, deck is created")
            logger.info("Handling 'decks/create, rendering create_deck.html")
            return render_template("create_deck.html", success=True)

        logger.error(
            "Handling 'decks/create, deck is not created")
        logger.info("Handling 'decks/create, rendering create_deck.html")
        return render_template("create_deck.html", success=False)

    logger.info("Handling 'decks/create, rendering create_deck.html")
    return render_template("create_deck.html", form=form)


@app.route("/decks/<int:deck_id>/delete")
@login_required
def delete_deck(deck_id):

    logger.info(f"Handling '/decks/{deck_id}/delete' route")

    if DecksRepository.delete(deck_id):
        logger.info(f"Handling '/decks/{deck_id}/delete' route, Deck with id {deck_id} has been deleted")
         
    logger.info(f"Handling '/decks/{deck_id}/delete' route, deck with id {deck_id} has not been deleted")

    return redirect(url_for("decks"))


@app.route("/decks/<int:deck_id>/cards/create", methods=["GET", "POST"])
@login_required
def create_card(deck_id: int):
    logger.info(
        f"Handling '/decks/{deck_id}/cards/create' route")

    form = CardForm(request.form)

    if request.method == "POST" and form.validate():

        word = form.word.data
        translation = form.translation.data

        logger.info(
            f"Handling '/decks/{deck_id}/cards/create' route, create_card form is submitted. Form details word: {word}, translation: {translation}")

        if not CardsRepository.create(deck_id, word, translation):
            logger.error(
                f"Handling '/decks/{deck_id}/cards/create' route, card has been not created")
            logger.info(
                f"Handling '/decks/{deck_id}/cards/create' route, rendering response")

            return "<h2>Card has been not created</h2>"

        logger.info(
            f"Handling '/decks/{deck_id}/cards/create' route, card is created")
        logger.info(
            f"Handling '/decks/{deck_id}/cards/create' route, rendering response")

        return "<h2>New card has been created</h2>"

    logger.info(
        f"Handling '/decks/{deck_id}/cards/create' route, rendering create_card.html")
    return render_template("create_card.html", form=form)

@app.route("/decks/<int:deck_id>/cards/<int:card_id>/delete")
def delete_card(deck_id: int, card_id: int):
    
    logger.info(f"Handling /decks/{deck_id}/cards/{card_id}/delete route")
    
    if CardsRepository.delete(card_id):
        logger.info(f"Handling /decks/{deck_id}/cards/{card_id}/delete route, card with id {card_id} has been deleted")
        return redirect(url_for("display_cards", deck_id = deck_id))
    logger.info(f"Handling /decks/{deck_id}/cards/{card_id}/delete, deck with id {card_id} has not been deleted")

    return redirect(url_for("display_cards", deck_id = deck_id))


@app.route("/decks/<int:deck_id>/cards/<int:card_id>/update", methods=["POST", "GET"])
def edit_card(deck_id: int, card_id: int):

    logger.info(f"Handling '/decks/{deck_id}/cards/{card_id}/update route")

    card = CardsRepository.get_by_id(card_id)

    form = CardForm(request.form)

   
    if request.method == "POST":
        
        word = form.word.data
        translation = form.translation.data

        logger.info(f"""Handling '/decks/{deck_id}/cards/{card_id}/update route, form has been submitted. 
        Form details word : {word}, translation : {translation}""")
        
        if CardsRepository.update(card_id, word, translation):
            logger.info("Handling '/decks/{deck_id}/cards/{card_id}/update route, card has been updated")

        logger.info("Handling '/decks/{deck_id}/cards/{card_id}/update route, card has not been updated")
        
        return redirect(url_for("card_detail", card_id = card_id, deck_id = deck_id))

    form.word.data = card.word
    form.word.translation = card.translation

    logger.debug("Handling '/decks/{deck_id}/cards/{card_id}/update route, rendering card_edit.html")

    return render_template("card_edit.html", form=form)
