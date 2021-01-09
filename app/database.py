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

    def __repr__(self):     # output of print()
        return f"User('{self.id}', '{self.username}', '{self.email}', '{self.password}')"


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
    name = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    dimension = db.Column(db.String(100), nullable=False)
    colors = db.Column(db.String(100), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id') , nullable=False)

    def __repr__(self):     # output of print()
          return f"Model('{self.id}', '{self.name}', '{self.description}', '{self.dimension}', '{self.colors}', '{self.creator_id}')"

class ModelPhoto(db.Model):
    image_name = db.Column(db.String(50), primary_key=True, nullable=False)  # 'maketaimg.jpg'
    video_name = db.Column(db.String(50), unique=True, nullable=False)         # 'video.mp4'
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable=False)

    def __repr__(self):     # output of print()
            return f"ModelPhoto('{self.image_name}', '{self.video_name}', '{self.model_id}')"

class ModelPrice(db.Model): 
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'))
    material = db.Column(db.String(20), nullable=False, primary_key=True)    # composite key?, static type for material?
    price = db.Column(db.Integer, nullable=False)    # need to add restriction for price>0    

    def __repr__(self):     # output of print()
          return f"ModelPrice('{self.model_id}', '{self.material}', '{self.price}')" 
                             
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):     # output of print()
          return f"Order('{self.id}', '{self.time_created}', '{self.user_id}')" 

# class OrderModel(db.Model):  #primary key nedostaje
#    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
#    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable=False)
#    material = db.Column(db.String(20), nullable=False)
#    price = db.Column(db.Integer, nullable=False)
#
#    def __repr__(self):     # output of print()
#        return f"OrderModel('{self.order_id}', '{self.model_id}', '{self.material}', '{self.price}')"
