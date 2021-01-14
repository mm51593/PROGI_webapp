from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
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

    def getNotifications(self):
        return ModelNotification.query.filter_by(receiver_id=self.id, seen=False).all()

    def __repr__(self):     # output of print()
        return f"User('{self.id}', '{self.username}', '{self.email}', '{self.password}')"

class Banned(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)

    def __repr__(self):     # output of print()
        return f"Banned('{self.id}', '{self.email}')"

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), nullable=False)
    author_id = db.Column(db.Integer, nullable=False)
    time_created = db.Column(db.DateTime, nullable=False)
    validated = db.Column(db.Boolean, nullable=False, default=False)
    def __repr__(self):
        return f"Story('{self.id}', '{self.title}')"


class StoryContent(db.Model):
    story_id = db.Column(db.Integer, primary_key=True)
    ordinal_number = db.Column(db.Integer, primary_key=True)
    story_text = db.Column(db.String(280))
    image_name = db.Column(db.String(50))
    video_name = db.Column(db.String(50))

    def __repr__(self):
        return f"StoryContent('{self.story_id}', '{self.ordinal_number}', '{self.story_text}', '{self.image_name}', '{self.video_name}')"

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    dimension = db.Column(db.String(100), nullable=False)
    colors = db.Column(db.String(100), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id') , nullable=False)
    approved = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):     # output of print()
          return f"Model('{self.id}', '{self.name}', '{self.description}', '{self.dimension}', '{self.colors}', '{self.creator_id}', '{self.approved}')"

class ModelPhoto(db.Model):
    image_name = db.Column(db.String(50), primary_key=True, nullable=False)  # 'maketaimg.jpg'
    #video_name = db.Column(db.String(50), unique=True, nullable=False)         # 'video.mp4'
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable=False)

    def __repr__(self):     # output of print()
            return f"ModelPhoto('{self.image_name}', '{self.model_id}')"

class ModelPrice(db.Model): 
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'))
    material = db.Column(db.String(20), nullable=False) #ne moze biti primary
    price = db.Column(db.Integer, nullable=False) 
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):     # output of print()
          return f"ModelPrice('{self.model_id}', '{self.material}', '{self.price}')" 

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140), nullable=False)
    author_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    id_story = db.Column(db.Integer, db.ForeignKey('story.id'), nullable=False)
    
    def __repr__(self):     # output of print()
          return f"Comment('{self.id}', '{self.text}', '{self.author}', '{self.timestamp}', '{self.id_story}' )"

class ModelNotification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    receiver_id = db.Column(db.Integer, nullable=False)
    model_id = db.Column(db.Integer, nullable=False)
    time_create = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    seen = db.Column(db.Boolean, nullable=False, default=False)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Ime = db.Column(db.String(25), nullable = True, default="")
    Private_ime = db.Column(db.Boolean, default = False)
    Prezime = db.Column(db.String, nullable = True, default="")
    Private_prezime = db.Column(db.Boolean, default = False)
    Datum_rodenja = db.Column(db.DateTime, nullable = True)
    Private_Datum = db.Column(db.Boolean, default = False)
    Zivotopis = db.Column(db.String(300), nullable = True, default="")
    Private_Zivotopis = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return f"Profile('{self.Ime}', '{self.Prezime}', '{self.Datum_rodenja}', '{self.Zivotopis}')"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    buyer_name = db.Column(db.String(40), nullable=False)
    buyer_email = db.Column(db.String(59), nullable=False)
    buyer_address = db.Column(db.String(100), nullable=False)

    def __repr__(self):     # output of print()
        return f"Order('{self.id}', '{self.time_created}', '{self.user_id}')"

class OrderModel(db.Model):  #primary key nedostaje
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable=False, primary_key=True)
    material = db.Column(db.String(20), nullable=False, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):     # output of print()
        return f"OrderModel('{self.order_id}', '{self.model_id}', '{self.material}', '{self.price}')"

class Cart(db.Model):
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True)

    def __repr__(self):     # output of print()
          return f"Cart('{self.buyer_id}')"

class CartModel(db.Model):
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.buyer_id'), nullable=False, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable=False, primary_key=True)
    material = db.Column(db.String(20), nullable=False, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):     # output of print()
        return f"CartModel('{self.cart_id}', '{self.model_id}', '{self.material}', '{self.price}')"

class PodaciPlacanje(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(70), nullable = True)
    email = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(30), nullable=True)
    country = db.Column(db.String(20), nullable = True)
    city = db.Column(db.String(20), nullable=True)
    zip_code = db.Column(db.String(8), nullable = True)
    card_full_name = db.Column(db.String(40), nullable = True)
    card_number = db.Column(db.String(20), nullable = True)
    card_expiry = db.Column(db.String(7), nullable = True)
    card_CVC = db.Column(db.String(3), nullable = True)

    def __repr__(self):
        return f"PodaciPlacanje('{self.Ime_Prezime}', '{self.email}', '{self.Ime_Kartica}', '{self.Broj_Kartica}')"

#ova linija mora biti na dnu datoteke
db.create_all()
