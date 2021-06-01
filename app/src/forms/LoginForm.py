from wtforms import Form, StringField, PasswordField, validators

from app.src.repositories import UsersRepository


class LoginForm(Form):

    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
