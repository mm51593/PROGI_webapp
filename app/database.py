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
	Prezime = db.Column(db.String, nullable = False)
	Datum_rodenja = db.Column(db.String(12), nullable = False)
	Zivotopis = db.Column(db.String(300), nullable = True)
