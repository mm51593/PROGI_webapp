from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.checkout.forms import CheckoutForm
from app.database import PodaciPlacanje, db

checkout = Blueprint('checkout', __name__)

@checkout.route('/checkout', methods=['GET','POST'])
def Checkout():
    form = CheckoutForm()
    billing_info = PodaciPlacanje.query.filter_by(id=current_user.id).first()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            billing_info.full_name = form.fname.data
            billing_info.email = form.email.data
            billing_info.address = form.adr.data
            billing_info.city = form.city.data
            billing_info.card_full_name = form.cname.data
            billing_info.card_number = form.ccnum.data
            billing_info.card_expiry = form.expmonth.data
            billing_info.country = form.state.data
            billing_info.zip_code = form.zip.data
            billing_info.CVC = form.cvv.data
            db.session.commit()
        flash ('Uspješno obavljena kupnja', 'success')
        return redirect(url_for('/'))
    elif request.method == 'GET':
        if current_user.is_authenticated:
            form.fname.data = billing_info.full_name
            form.email.data = billing_info.email
            form.adr.data = billing_info.address
            form.city.data = billing_info.city
            form.cname.data = billing_info.card_full_name
            form.ccnum.data = billing_info.card_number
            form.expmonth.data = billing_info.card_expiry
            form.state.data = billing_info.country
            form.zip.data = billing_info.zip_code
            form.cvv.data = billing_info.CVV
    else:
        print(form.errors)
    return render_template('checkout.html',title = "Podaci za placanje", form = form)
