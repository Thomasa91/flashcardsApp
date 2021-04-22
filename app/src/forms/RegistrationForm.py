from wtforms import Form, StringField, PasswordField, validators
from app.src.validators import email_validator, password_validator, date_validator
from wtforms.fields.html5 import DateField

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=6, max=25),])
    email = StringField('Email', [email_validator(),])
    password = PasswordField('Password', [password_validator(), ])
    birthday = DateField("Enter your birthday", [date_validator(), ], format='%Y-%m-%d')