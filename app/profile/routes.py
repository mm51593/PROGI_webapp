from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.profile.forms import UpdateForm
from app.database import db

profile = Blueprint('profile', __name__)

@profile.route('/User')
@login_required
def User():
    return render_template ('korracun_prikaz.html', title = 'korisnički podaci')

@profile.route('/UserChange', methods=['GET','POST'])
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
