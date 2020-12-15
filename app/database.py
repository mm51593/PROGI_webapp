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

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=True)          # nullable could later be omitted, description size = 500 for now
    creator_id = db.Column(db.Integer, db.Foreign_Key('user.id') , nullable=False)

    def __repr__(self):     # output of print()
          return f"Model('{self.id}', '{self.name}', '{self.description}', '{self.creator_id}')"

class ModelPhoto(db.Model):
    image_name = db.Column(db.String(50), primary_key=True, nullable=False)  # 'maketaimg.jpg'
    model_id = db.Column(db.Integer, db.Foreign_Key('model.id'), nullable=False)

    def __repr__(self):     # output of print()
            return f"ModelPhoto('{self.image_name}', '{self.model_id}')"

class ModelPrice(db.Model): 
    model_id = db.Column(db.Integer, db.Foreign_Key('model.id'), primary_key=True) 
    material = db.Column(db.String(20), nullable=False)    # composite key?, static type for material?
    price = db.Column(db.Integer, nullable=False)    # need to add restriction for price>0    

    def __repr__(self):     # output of print()
          return f"ModelPrice('{self.model_id}', '{self.material}', '{self.price}')" 
                             

class OrderModel(db.Model):
    order_id = db.Column(db.Integer, db.Foreign_Key('order.id'), nullable=False)
    model_id = db.Column(db.Integer, db.Foreign_Key('model.id'), nullable=False)
    material = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)  # numeric type instead of integer?

    def __repr__(self):     # output of print()
        return f"OrderModel('{self.order_id}', '{self.model_id}', '{self.material}', '{self.price}')"



#products = {
#        'name': 'Maketa 1',
#        'description': 'blablabla bla',
#        'price': '100',
#        'image_file': '',
#        'material': ''
#    }

    