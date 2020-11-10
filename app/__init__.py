from flask import Flask
from flask_login import LoginManager

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dummy.db'
application.config['SECRET_KEY'] = 'secret-key'
login_manager = LoginManager(application)


from app import database
from app import routes
from app.authentication.routes import authentication

application.register_blueprint(authentication)
#application.store_blueprint(store)