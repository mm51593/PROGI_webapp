from flask import Blueprint, render_template, redirect, request, url_for, send_from_directory, abort
from app.database import  User, db, Banned
from flask_login import current_user

admin = Blueprint('admin', __name__)

@admin.route('/admin', methods=['GET', 'POST'])
def admin_index():
    if current_user.id == 1:
        return render_template('adminpage.html')
    else:
        abort(404)


# @admin.route('/admin/transakcije')
# def admin_transakcije():
#     if current_user.id == 1:
#         transakcije = OrderModel.query.all() #provizorno!
#         return render_template('transakcije.html', title='Lista transakcija',  transakcije=transakcije) #potrebna je html tablica
#     else:
#         abort(404)
#TODO: DODAJ JOS LINK U HTML


@admin.route('/admin/userlist')
def admin_userlist():
    if current_user.id == 1:
        users = User.query.all()
        return render_template('lista_korisnika.html', title='Lista korisnika', users=users) #TODO: PROMIJENI HYPERLINK U HTMLU DA EKSLI IDE NA USER PAGE
    else:
        abort(404)

@admin.route('/admin/ban/<user_id>')
def admin_ban(user_id):
    banuser = User.query.filter_by(id=user_id).first()
    banneduser = Banned(email=banuser.email)
    db.session.delete(banuser)
    db.session.commit()
    db.session.add(banneduser)
    db.session.commit()
    return redirect(url_for('admin.admin_userlist'))