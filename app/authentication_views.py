from flask import render_template, request
from app import app



@app.route("/register", methods=["POST" ,"GET"])
def register():
    return "register"


@app.route("/login", methods=["POST", "GET"])
def login():
    return "login"