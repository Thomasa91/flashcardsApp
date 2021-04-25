from wtforms import Form, StringField, validators, ValidationError


class DeckForm(Form):

    name = StringField("Name", [validators.InputRequired(), validators.length(max=64)])