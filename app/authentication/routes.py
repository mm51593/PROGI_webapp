from flask import Blueprint, render_template, redirect, url_for, request
from app.authentication.forms import RegistrationForm, LoginForm
from app.database import User, db, bcrypt, Profile
from flask_login import login_user, current_user, logout_user

authentication = Blueprint('auth', __name__)


@authentication.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        print("success")
        hashed_pass = bcrypt.generate_password_hash(reg_form.password.data)
        user = User(username=reg_form.username.data, email=reg_form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        profile = Profile(id=user.id)
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('auth.login'))
    else:
        print(reg_form.errors)
    return render_template("registracija.html", title="Registriraj se", form=reg_form)


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    login_form = LoginForm()
    login_error = None
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=login_form.remember.data)
            return redirect(request.referrer)
        else:
            login_error = "Neispravna E-mail adresa ili lozinka."
            print(login_error)
    return render_template("prijava.html", title="Prijavi se", form=login_form, error=login_error)


@authentication.route('/logout')
def logout():
    logout_user()
    return redirect('/')
