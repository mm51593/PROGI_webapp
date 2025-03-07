from flask import Blueprint, render_template, redirect, request, url_for, send_from_directory, abort, flash
from app.database import  User, db, Banned, Order, OrderModel, Model
from flask_login import current_user

admin = Blueprint('admin', __name__)

@admin.route('/admin', methods=['GET', 'POST'])
def admin_index():
    if current_user.is_authenticated:
        if current_user.id == 1:
            return render_template('adminpage.html')
    abort(404)

@admin.route('/admin/transakcije')
def admin_transakcije():
    if current_user.id == 1:
        transakcije = Order.query.all() #provizorno!
        for elem in transakcije:
            if elem.user_id == 0:
                elem.username = "Neregistrirani korisnik"
            else:
                elem.username = User.query.filter_by(id=elem.user_id).first().username
        return render_template('transakcije.html', title='Lista transakcija',  transakcije=transakcije) #potrebna je html tablica
    else:
        abort(404)

@admin.route('/transakcija/<int:transaction_id>')
def transakcije_pojedinacno(transaction_id):
    if current_user.id == 1:
        order = Order.query.filter_by(id=transaction_id).first()
        models = OrderModel.query.filter_by(order_id=transaction_id).all()
        price = 0
        for elem in models:
            elem.model_name = Model.query.filter_by(id=elem.model_id).first().name
            price += elem.price * elem.quantity
        return render_template('transakcije_pojedinacno.html', title='Transakcija ' + str(transaction_id), models=models, order=order, price=price)
    else:
        abort(404)

@admin.route('/admin/userlist')
def admin_userlist():
    if current_user.is_authenticated:
        if current_user.id == 1:
            users = User.query.all()
            return render_template('lista_korisnika.html', title='Lista korisnika', users=users)
    abort(404)

@admin.route('/admin/ban/<int:user_id>')
def admin_ban(user_id):
    print(user_id)
    if user_id == 1:
        flash("Adminu ne može biti zabranjen pristup")
    else:
        banuser = User.query.filter_by(id=user_id).first()
        banneduser = Banned(email=banuser.email)
        db.session.delete(banuser)
        db.session.commit()
        db.session.add(banneduser)
        db.session.commit()
    return redirect(url_for('admin.admin_userlist'))