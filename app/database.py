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

class Product(db.Model):
    id_p = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=True)          # nullable could later be omitted, description size = 500 for now
    price = db.Column(db.Integer, nullable=False)                   # need to add restriction for price>0
    image_file = db.Column(db.String(20), nullable=False, default='maketaimg.jpg')      # 'maketaimg.jpg' as current placeholder
    material = db.Column(db.String(20))                             # default value could be added, material to be implemented as static type?, nullable could be implemeted

    def __repr__(self):     # output of print()
        return f"Product('{self.id_p}', '{self.name}', '{self.description}', '{self.price}', '{self.image_file}', '{self.material}')"

products = {
        'name': 'Maketa 1',
        'description': 'blablabla bla',
        'price': '100',
        'image_file': '',
        'material': ''
    }

    