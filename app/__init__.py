from flask import Flask
from flask_login import LoginManager

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dummy.db'
application.config['SECRET_KEY'] = 'secret-key'
login_manager = LoginManager(application)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from app import database
from app import routes
from app.authentication.routes import authentication

application.register_blueprint(authentication)