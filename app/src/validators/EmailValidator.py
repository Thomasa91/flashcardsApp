from email_validator import validate_email as check_email, EmailNotValidError
from wtforms import ValidationError


class EmailValidator():

    def __init__(self, message="Email is not valid"):
        self.message = message

    def __call__(self, form, field):

        check_email(field.data)
