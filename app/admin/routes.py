from flask import Blueprint, render_template, redirect, request, url_for, send_from_directory, abort
from app.database import  OrderModel, User, db

admin = Blueprint('admin', __name__)

@admin.route('/admin', methods=['GET', 'POST'])
def admin_index():
    return render_template('adminpage.html') #potreban je html

@admin.route('/admin/transakcije')
def admin_transakcije():
    transakcije = OrderModel.query.all() #provizorno!
    return render_template('transakcije.html', transakcije=transakcije) #potrebna je html tablica

@admin.route('/admin/userlist')
def admin_userlist():
    users = User.query.all()
    return render_template('lista_koristnika.html', users=users) #potreban je html za ispisivanje liste usera