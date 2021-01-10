from flask import Flask
from flask_login import LoginManager

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dummy.db'
application.config['SECRET_KEY'] = 'secret-key'
application.config['STORY_LOCATION'] = 'static/story_files'
login_manager = LoginManager(application)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from app import database
from app import routes
from app.authentication.routes import authentication
from app.profile.routes import profile
from app.checkout.routes import checkout

application.register_blueprint(authentication)
application.register_blueprint(profile)
application.register_blueprint(checkout)