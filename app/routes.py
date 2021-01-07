from app import application, database
from flask import Blueprint, render_template, redirect, url_for, redirect, request, flash
from app.database import User, db, bcrypt, Model, ModelPhoto, ModelPrice, Order

#@application.route('/')
#@application.route('/index')
#def index():
#    return "Hello world"


@application.route('/')
@application.route('/makete_prikaz', methods=['GET', 'POST'])
#@login_required
def makete_prikaz_Instance():
    models = Model.query.all()
    return render_template('makete_prikaz.html', title='Makete', models=models)
