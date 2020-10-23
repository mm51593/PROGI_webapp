from flask_sqlalchemy import SQLAlchemy
from app import application
db = SQLAlchemy(application)

class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):     # output of print()
        return f"User('{self.userID}', '{self.username}', '{self.email}', '{self.password}')"
