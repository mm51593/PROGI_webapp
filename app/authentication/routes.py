from flask import Blueprint, render_template, redirect, url_for , request
from app.authentication.forms import RegistrationForm, LoginForm, UpdateForm
from app.database import User, db, bcrypt, UserPodaci
from flask_login import login_user, current_user, logout_user, login_required

authentication = Blueprint('auth', __name__)


@authentication.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(reg_form.password.data)
        user = User(username=reg_form.username.data, email=reg_form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('/auth.login'))
    return render_template("registracija.html", title="Registriraj se", form=reg_form)


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=login_form.remember.data)
            return redirect('/')
    return render_template("prijava.html", title="Prijavi se", form=login_form)


@authentication.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@authentication.route('/User')
@login_required
def User():
    return render_template ('korracun_prikaz.html', title = 'korisnički podaci')

@authentication.route('/UserChange', methods=['GET','POST'])
def Change():
    form = UpdateForm()
    if form.validate_on_submit():
        current_user.Ime = form.Ime.data
        current_user.Private_Ime = form.Private_Ime.data
        current_user.Prezime = form.Prezime.data
        current_user.Private_Prezime = form.Private_Prezime.data
        current_user.DatumRodenja = form.DatumRodenja.data
        current_user.Private_Datum = form.Private_Datum.data
        current_user.Zivotopis = form.Zivotopis.data
        current_user.Private_Zivotopis = form.Private_Zivotopis.data
        db.session.commit()
        flash ('Promijenili ste podatke korisničkog računa', 'success')
        return redirect(url_for('/User'))
    elif request.method == 'GET':
        form.Ime.data = current_user.Ime
        form.Private_Ime.data = False
        form.Prezime.data = current_user.Prezime
        form.Private_Prezime.data = False
        form.DatumRodenja.data = current_user.DatumRodenja
        form.Private_Datum.data = False
        form.Zivotopis.data = current_user.Zivotopis
        form.Private_Zivotopis.data = False
    return render_template('korracun_izmjena.html',title = "Izmjeni korisničke podatke", form = form)