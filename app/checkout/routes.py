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
            billing_info.Ime_Prezime = form.fname.data
            billing_info.email = form.email.data
            billing_info.Adresa = form.adr.data
            billing_info.Grad = form.city.data
            billing_info.Ime_Kartica = form.cname.data
            billing_info.Broj_Kartica = form.ccnum.data
            billing_info.Datum_Isteka = form.expmonth.data
            billing_info.Drzava = form.state.data
            billing_info.Postanski_Broj = form.zip.data
            billing_info.Godina_Isteka = form.expyear.data
            billing_info.CVV = form.cvv.data
            db.session.commit()
        flash ('Uspješno obavljena kupnja', 'success')
        return redirect(url_for('/'))
    elif request.method == 'GET':
        if current_user.is_authenticated:
            form.fname.data = billing_info.Ime_Prezime
            form.email.data = billing_info.email
            form.adr.data = billing_info.Adresa
            form.city.data = billing_info.Grad
            form.cname.data = billing_info.Ime_Kartica
            form.ccnum.data = billing_info.Broj_Kartica
            form.ccnum.data = billing_info.Datum_Isteka
            form.expmonth.data = billing_info.Datum_Isteka
            form.state.data = billing_info.Drzava
            form.zip.data = billing_info.Postanski_Broj
            form.expyear.data = billing_info.Godina_Isteka
            form.cvv.data = billing_info.CVV
    else:
        print(form.errors)
    return render_template('checkout.html',title = "Podaci za placanje", form = form)
