from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.checkout.forms import CheckoutForm
from app.database import PodaciPlacanje

checkout = Blueprint('checkout', __name__)

@checkout.route('/checkout', methods=['GET','POST'])
def Checkout():
    form = CheckoutForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            profile = PodaciPlacanje.query.filter_by(id=current_user.id).first()
            profile.Ime_Prezime = form.fname.data
            profile.email = form.email.data
            profile.Adresa = form.adr.data
            profile.Grad = form.city.data
            profile.Ime_Kartica = form.cname.data
            profile.Broj_Kartica = form.ccnum.data
            profile.Datum_Isteka = form.expmonth.data
            profile.Drzava = form.state.data
            profile.Postanski_Broj = form.zip.data
            profile.Godina_Isteka = form.expyear.data
            profile.CVV = form.cvv.data
            db.session.commit()
        flash ('Uspješno obavljena kupnja', 'success')
        return redirect(url_for('/'))
    elif request.method == 'GET':
        if current_user.is_authenticated:
            form.fname.data = profile.Ime_Prezime
            form.email.data = profile.email
            form.adr.data = profile.Adresa
            form.city.data = profile.Grad
            form.cname.data = profile.Ime_Kartica
            form.ccnum.data = profile.Broj_Kartica
            form.ccnum.data = profile.Datum_Isteka
            form.expmonth.data = profile.Datum_Isteka
            form.state.data = profile.Drzava
            form.zip.data = profile.Postanski_Broj
            form.expyear.data = profile.Godina_Isteka
            form.cvv.data = profile.CVV
    else:
        print(form.errors)
    return render_template('checkout.html',title = "Podaci za placanje", form = form)
