from flask import Blueprint, render_template, redirect, request, url_for, send_from_directory, abort
from app.database import  OrderModel, User, db
from flask_login import current_user

admin = Blueprint('admin', __name__)

@admin.route('/admin', methods=['GET', 'POST'])
def admin_index():
    if current_user.id == 1:
        return render_template('adminpage.html') #potreban je html
    else:
        abort(404)


@admin.route('/admin/transakcije')
def admin_transakcije():
    if current_user.id == 1:
        transakcije = OrderModel.query.all() #provizorno!
        return render_template('transakcije.html', title='Lista transakcija',  transakcije=transakcije) #potrebna je html tablica
    else:
        abort(404)


@admin.route('/admin/userlist')
def admin_userlist():
    if current_user.id == 1:
        users = User.query.all()
        return render_template('lista_koristnika.html', title='Lista korisnika', users=users) #potreban je html za ispisivanje liste usera
    else:
        abort(404)
