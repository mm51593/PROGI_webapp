from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app import application, login_manager
from flask_login import UserMixin
import datetime
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)


@login_manager.user_loader
def load_user(user_userID):
    return User.query.get(int(user_userID))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):     # output of print()
        return f"User('{self.id}', '{self.username}', '{self.email}', '{self.password}')"

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Ime = db.Column(db.String(25), nullable = True)
    Private_ime = db.Column(db.Boolean, default = False)
    Prezime = db.Column(db.String, nullable = True)
    Private_prezime = db.Column(db.Boolean, default = False)
    Datum_rodenja = db.Column(db.DateTime, nullable = True, default = datetime.datetime.utcnow)
    Private_Datum = db.Column(db.Boolean, default = False)
    Zivotopis = db.Column(db.String(300), nullable = True)
    Private_Zivotopis = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return f"Profile('{self.Ime}', '{self.Prezime}', '{self.Datum_rodenja}', '{self.Zivotopis}')"

class PodaciPlacanje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Ime_Prezime = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(50), nullable=False)
    Adresa = db.Column(db.String(30), nullable=False)
    Grad = db.Column(db.String(20), nullable=False)
    Ime_Kartica = db.Column(db.String(40), default = "Pero Perić" , nullable = False)
    Broj_Kartica = db.Column(db.String(20), default = "1111-2222-3333-4444" , nullable = False)
    Datum_Isteka = db.Column(db.String(10), default = "studeni" , nullable = False)
    Drzava = db.Column(db.String(20), default = "Hrvatska" , nullable = False)
    Postanski_Broj = db.Column(db.String(8), default = "10000" , nullable = False)
    Godina_Isteka = db.Column(db.String(5), default = "2022" , nullable = False)
    CVV = db.Column(db.String(3), default = "352" , nullable = False)

    def __repr__(self):
        return f"PodaciPlacanje('{self.Ime_Prezime}', '{self.email}', '{self.Ime_Kartica}', '{self.Broj_Kartica}')"