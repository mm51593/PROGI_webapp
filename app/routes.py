from app import application, database
from flask import Blueprint, render_template, redirect, url_for, redirect, request, flash
from app.database import User, db, bcrypt, Product, products

#@application.route('/')
#@application.route('/index')
#def index():
#    return "Hello world"


@application.route('/')
@application.route('/makete_prikaz')    #samo GET metoda dovoljna
def makete_prikaz():
    prod = Product.query.all()
    return render_template("makete_prikaz.html", prod=products, title="Makete")
