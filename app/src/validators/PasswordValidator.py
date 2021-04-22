from wtforms import ValidationError
import re


class PasswordValidator():

    def __init__(self, min=8, max=64,):
        self.min = min
        self.max = max

    def __call__(self, form, field):

        length = len(field.data)

        if length < self.min or length > self.max:
            raise ValidationError(
                f'Password has to be between {self.min} - {self.max} characters')

        if not re.search(r"[A-Z]", field.data):
            raise ValidationError(
                'Passoword has to have at least one capital letter')

        if not re.search(r"[a-z]", field.data):
            raise ValidationError(
                'Password has to have at least one small letter')

        if not re.search(r"\d", field.data):
            raise ValidationError('Password has to have at least one number')
