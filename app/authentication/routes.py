from flask import Blueprint
from app.authentication.forms import RegistrationForm, LoginForm
from app.database import User, db
from flask_login import login_user

authentication = Blueprint('auth', __name__)


@authentication.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        user = User(username=reg_form.username.data, email=reg_form.email.data, password=reg_form.password.data)
        db.session.add(user)
        db.session.commit()
    return "register.html"


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(emal=login_form.email.data).first()
        if user and user.password == login_form.password.data:
            login_user(user, remember=login_form.remember.data)
    return "login.html"
