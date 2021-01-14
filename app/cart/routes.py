from flask import Blueprint, render_template, session
from sqlalchemy import exc
from app.database import db, Model, Cart, CartModel
from flask_login import login_user, current_user, logout_user

cart = Blueprint('cart', __name__)

@cart.route('/cart', methods=['GET', 'POST'])
#@login_required
def cart_Instance():
    models = []
    if current_user.is_authenticated:
        cart_inst = Cart.query.filter_by(buyer_id=current_user.id).first()
        if cart_inst is None:
            cart_inst = Cart(buyer_id=current_user.id)
            db.session.add(cart_inst)
            try:
                db.session.commit()
            except exc.SQLAlchemyError:
                pass
        contents = CartModel.query.filter_by(cart_id=cart_inst.buyer_id).all()
        for content in contents:
            model_elem = Model.query.filter_by(id=content.model_id).first()
            models.append(model_elem)
    else:
        if session.get('cart', None) is None:
            session['cart'] = []
        contents = session['cart']
        for elem in contents:
            model_elem = Model.query.filter_by(id=elem['model_id']).first()
            models.append(model_elem)
    return render_template('cart.html', title='Košarica', contents=contents, models=models, number=len(contents))
