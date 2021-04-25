from wtforms import Form, StringField, PasswordField, validators, ValidationError
from wtforms.fields.html5 import DateField
from email_validator import validate_email as check_email
from datetime import date
from app.src.utilities.logger import logger
from app.src.repositories import UsersRepository

import re


def username_validator(form, field):

    if UsersRepository.get_by_username(field.data):
        raise ValidationError("Username already exists")


def email_validator(form, field):
    check_email(field.data)

    if UsersRepository.get_by_email(field.data):
        raise ValidationError("Email is already used")


def password_validator(min, max):

    def _password_validator(form, field):

        length = len(field.data)

        if length < min or length > max:
            raise ValidationError(
                f'Password has to be between {min} - {max} characters')

        if not re.search(r"[A-Z]", field.data):
            raise ValidationError(
                'Passoword has to have at least one capital letter')

        if not re.search(r"[a-z]", field.data):
            raise ValidationError(
                'Password has to have at least one small letter')

        if not re.search(r"\d", field.data):
            raise ValidationError('Password has to have at least one number')

    return _password_validator


def birthday_validator(form, field):

    input_date = field.data

    if input_date.year < 1900:
        raise ValidationError("Year has to be bigger than 1900")

    if date.today() < input_date:
        raise ValidationError("Are you from the future?")


class RegistrationForm(Form):
    username = StringField(
        'Username', [validators.Length(min=6, max=25), validators.InputRequired(), username_validator])
    email = StringField('Email', [validators.InputRequired(), email_validator])
    password = PasswordField(
        'Password', [validators.InputRequired(), password_validator(8, 64), ])
    birthday = DateField("Enter your birthday", [validators.InputRequired(),
                         birthday_validator, ], format='%Y-%m-%d')
