from app import application
from flask import Flask, render_template, url_for

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', title='Početna')
