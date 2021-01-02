from app import application
from flask import Blueprint, render_template, redirect, request, url_for, send_from_directory, Flask

index = Blueprint('index', __name__)

@index.route('/')
def homepage():
    return render_template("index.html", title="Home")
