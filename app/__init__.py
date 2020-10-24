from flask import Flask

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dummy.db'
application.config['SECRET_KEY'] = 'secret-key'
from app import database
from app import routes
from app.authentication.routes import authentication

application.register_blueprint(authentication)