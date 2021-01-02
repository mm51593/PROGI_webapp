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


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), nullable=False)
    author_id = db.Column(db.Integer, nullable=False)
    time_created = db.Column(db.DateTime, nullable=False)
    validated = db.Column(db.Boolean, nullable=False)
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
