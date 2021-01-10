from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.profile.forms import UpdateForm
from app.database import db, Profile

profile = Blueprint('profile', __name__)

@profile.route('/Profil')
def Profil():
    user_profile = Profile.query.filter_by(id=current_user.id).first()
    user_profile.Private_Ime = False
    user_profile.Private_Prezime = False
    user_profile.Private_Datum = False
    user_profile.Private_Zivotopis = False
    print(user_profile)
    return render_template ('korracun_prikaz.html', title = 'Korisnički podaci', profile=user_profile)

@profile.route('/Profil/<id>')
def User_Profil(id):
    user_profile = Profile.query.filter_by(Profile.id == id).first()
    print(user_profile)
    return render_template ('tudi_korracun_prikaz.html', title = 'Korisnički podaci', profile=user_profile)


@profile.route('/UserChange', methods=['GET','POST'])
def Change():
    form = UpdateForm()
    user_profile = Profile.query.filter_by(id=current_user.id).first()
    if form.validate_on_submit():
        user_profile.Ime = form.Ime.data
        user_profile.Private_Ime = form.Private_Ime.data
        user_profile.Prezime = form.Prezime.data
        user_profile.Private_Prezime = form.Private_Prezime.data
        user_profile.Datum_rodenja = form.Datum_rodenja.data
        user_profile.Private_Datum = form.Private_Datum.data
        user_profile.Zivotopis = form.Zivotopis.data
        user_profile.Private_Zivotopis = form.Private_Zivotopis.data
        db.session.commit()
        flash ('Promijenili ste podatke korisničkog računa', 'success')
        return redirect(url_for('profile.Profil'))
    elif request.method == 'GET':
        form.Ime.data = user_profile.Ime
        form.Private_Ime.data = False
        form.Prezime.data = user_profile.Prezime
        form.Private_Prezime.data = False
        form.Datum_rodenja.data = user_profile.Datum_rodenja
        form.Private_Datum.data = False
        form.Zivotopis.data = user_profile.Zivotopis
        form.Private_Zivotopis.data = False
    else:
        print(form.errors)
    return render_template('korracun_izmjena.html',title = "Izmjeni korisničke podatke", form = form)
