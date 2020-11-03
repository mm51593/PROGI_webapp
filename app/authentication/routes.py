from flask import Blueprint, render_template
from app.authentication.forms import RegistrationForm, LoginForm
from app.database import User, db, bcrypt
from flask_login import login_user

authentication = Blueprint('auth', __name__)


@authentication.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(reg_form.password.data)
        user = User(username=reg_form.username.data, email=reg_form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
    else:
        print(reg_form.errors)
    return render_template("registracija.html", title="Registriraj", form=reg_form)


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(emal=login_form.email.data).first()
        if user and user.password == login_form.password.data:
            login_user(user, remember=login_form.remember.data)
    return "login.html"
