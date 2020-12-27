from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app import application, login_manager
from flask_login import UserMixin
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

class UserPodaci(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Ime = db.Column(db.String(25), nullable = False)
    Private_ime = db.Column(db.Boolean, default = False)
    Prezime = db.Column(db.String, nullable = False)
    Private_prezime = db.Column(db.Boolean, default = False)
    Datum_rodenja = db.Column(db.String(12), nullable = False)
    Private_Datum = db.Column(db.Boolean, default = False)
    Zivotopis = db.Column(db.String(300), nullable = True)
    Private_Zivotopis = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return f"UserPodaci('{self.Ime}', '{self.Prezime}', '{self.Datum_rodenja}', '{self.Zivotopis}')"
