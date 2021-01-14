from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import current_user
from app.checkout.forms import CheckoutForm
from app.database import PodaciPlacanje, db, Cart, CartModel, Order, OrderModel

checkout = Blueprint('checkout', __name__)

@checkout.route('/checkout', methods=['GET','POST'])
def checkout_page():
    form = CheckoutForm()
    if form.validate_on_submit():
        if current_user.is_authenticated and form.remember:
            billing_info = PodaciPlacanje.query.filter_by(user_id=current_user.id).first()
            billing_info.full_name = form.fname.data
            billing_info.email = form.email.data
            billing_info.address = form.adr.data
            billing_info.city = form.city.data
            billing_info.card_full_name = form.cname.data
            billing_info.card_number = form.ccnum.data
            billing_info.card_expiry = form.expdate.data
            billing_info.country = form.state.data
            billing_info.zip_code = form.zip.data
            billing_info.card_CVC = form.cvv.data
            db.session.commit()
        flush_cart(form)
        flash ('Uspješno obavljena kupnja', 'success')
        return redirect(url_for('index.homepage'))
    elif request.method == 'GET':
        if current_user.is_authenticated:
            billing_info = PodaciPlacanje.query.filter_by(user_id=current_user.id).first()
            form.fname.data = billing_info.full_name
            form.email.data = billing_info.email
            form.adr.data = billing_info.address
            form.city.data = billing_info.city
            form.cname.data = billing_info.card_full_name
            form.ccnum.data = billing_info.card_number
            form.expdate.data = billing_info.card_expiry
            form.state.data = billing_info.country
            form.zip.data = billing_info.zip_code
            form.cvv.data = billing_info.card_CVC
    else:
        print(form.errors)
    return render_template('checkout.html',title = "Podaci za placanje", form = form)

def flush_cart(form):
    buyer_name = form.fname.data
    buyer_email = form.email.data
    buyer_address = form.adr.data + ', ' + form.zip.data + ' ' + form.city.data + ', ' + form.state.data
    if current_user.is_authenticated:
        cart = Cart.query.filter_by(buyer_id=current_user.id).first()
        order = Order(user_id=current_user.id, buyer_name=buyer_name, buyer_email=buyer_email, buyer_address=buyer_address)
        cart_contents = CartModel.query.filter_by(cart_id=cart.buyer_id).all()
        print(cart)
        db.session.delete(cart)
    else:
        cart_contents = list(session['cart'])
        order = Order(user_id=0, buyer_name=buyer_name, buyer_email=buyer_email, buyer_address=buyer_address)
        del session['cart']

    db.session.add(order)
    db.session.commit()

    if current_user.is_authenticated:
        for elem in cart_contents:
            order_elem = OrderModel(order_id=order.id, model_id=elem.model_id, material=elem.material, price=elem.price, quantity=elem.quantity)
            db.session.add(order_elem)
            db.session.delete(elem)
    else:
        for elem in cart_contents:
            order_elem = OrderModel(order_id=order.id, model_id=elem.get('model_id'), material=elem.get('material'),
                            price=elem.get('price'), quantity=elem.get('quantity'))
            db.session.add(order_elem)
            db.session.delete(elem)
    db.session.commit()
    return
