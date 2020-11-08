from flask import Flask
from flask_login import LoginManager

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dummy.db'
application.config['SECRET_KEY'] = 'secret-key'
application.config['STORY_LOCATION'] = r'./app/static/story_files'
login_manager = LoginManager(application)


from app import database
from app import routes
from app.authentication.routes import authentication
from app.stories.routes import stories

application.register_blueprint(authentication)
application.register_blueprint(stories)