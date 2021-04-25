from wtforms import Form, StringField, TextAreaField, validators, ValidationError
import re


def word_validator(form, field):

    only_letters_pattern = r"[A-Za-z]+"

    if not re.match(only_letters_pattern, field.data):
        raise ValidationError("Field only accepts letters")


class CardForm(Form):

    word = StringField('Word', [validators.InputRequired(), word_validator])
    translation = TextAreaField(
        "Meaning", [validators.InputRequired(), validators.length(max=150)])
