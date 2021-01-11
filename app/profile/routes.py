from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.profile.forms import UpdateForm
from app.database import db, Profile, User

profile = Blueprint('profile', __name__)

#@profile.route('/Profil')
#def Profil():
#    user_profile = Profile.query.filter_by(id=current_user.id).first()
#    user_profile.Private_Ime = False
#    user_profile.Private_Prezime = False
#    user_profile.Private_Datum = False
#    user_profile.Private_Zivotopis = False
#    print(user_profile)
#    return render_template ('korracun_prikaz.html', title = 'Korisnički podaci', profile=user_profile)

@profile.route('/profil/<id>')
def User_Profil(id):
    user_profile = Profile.query.filter_by(id=id).first()
    user = User.query.filter_by(id=id).first()
    print(user.id)
    return render_template ('tudi_korracun_prikaz.html', title = 'Korisnički podaci', profile=user_profile, user=user)


@profile.route('/urediprofil', methods=['GET','POST'])
def Change():
    form = UpdateForm()
    user_profile = Profile.query.filter_by(id=current_user.id).first()
    if form.validate_on_submit():
        user_profile.Ime = form.Ime.data
        user_profile.Private_ime = form.Private_Ime.data
        user_profile.Prezime = form.Prezime.data
        user_profile.Private_prezime = form.Private_Prezime.data
        user_profile.Datum_rodenja = form.Datum_rodenja.data
        user_profile.Private_Datum = form.Private_Datum.data
        user_profile.Zivotopis = form.Zivotopis.data
        user_profile.Private_Zivotopis = form.Private_Zivotopis.data
        flash ('Promijenili ste podatke korisničkog računa', 'success')
        db.session.commit()
        return redirect(url_for('profile.User_Profil', id=current_user.id))
    elif request.method == 'GET':
        form.Ime.data = user_profile.Ime
        form.Private_Ime.data = user_profile.Private_ime
        form.Prezime.data = user_profile.Prezime
        form.Private_Prezime.data = user_profile.Private_prezime
        form.Datum_rodenja.data = user_profile.Datum_rodenja
        form.Private_Datum.data = user_profile.Private_Datum
        form.Zivotopis.data = user_profile.Zivotopis
        form.Private_Zivotopis.data = user_profile.Private_Zivotopis
    else:
        print(form.errors)
    return render_template('korracun_izmjena.html',title = "Izmjeni korisničke podatke", form = form)
