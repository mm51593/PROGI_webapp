from flask import Blueprint, render_template, redirect, url_for, redirect, request, flash
from app.database import User, db, bcrypt, Product

store = Blueprint('store', __name__)

@store.route('/products', methods=['GET', 'POST'])    #samo GET metoda dovoljna
def render():
    prod = Product.query.all()
    return render_template("makete_prikaz.html", prod=products, title="Makete")






@store.route('/material', methods=['GET', 'POST'])
def updatePrice():
    pass