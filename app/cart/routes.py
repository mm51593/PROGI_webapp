from flask import Blueprint, render_template, redirect, url_for, redirect, request, flash
from sqlalchemy import exc
from app.database import User, db, bcrypt, Model, ModelPhoto, ModelPrice, Cart, CartModel, Order #OrderModel
from app import application
from flask_login import login_user, current_user, logout_user
from uuid import uuid4
from os import path, listdir

cart = Blueprint('cart', __name__)

@store.route('/cart', methods=['GET', 'POST'])
#@login_required
def cart_Instance():
    models = []
    cart_inst = Cart.query.filter_by(buyer_id=current_user.id).first()
    if cart_inst == None:
        cart_inst = Cart(buyer_id=current_user.id)
        db.session.add(cart_inst)
        try:
            db.session.commit()
        except exc.SQLAlchemyError:
            pass   
    contents = CartModel.query.filter_by(cart_id=cart_inst.id).all()
    for content in contents:
        model_elem = Model.query.filter_by(id=content.model_id).first()
        models.append(model_elem)
    #model_elem = Model.query.filter_by(id=contents.model_id).all()
    #model_len = len(models)
    return render_template('cart.html', title='Košarica', contents=contents, models=models)