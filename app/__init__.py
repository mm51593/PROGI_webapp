from flask import Flask
from flask_login import LoginManager

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dummy.db'
application.config['SECRET_KEY'] = 'secret-key'
application.config['STORY_LOCATION'] = 'static/story_files'
application.config['MODEL_LOCATION'] = 'static/model_files'
application.config['MATERIALS'] = ['Drvo', 'Aluminij', 'Željezo']
login_manager = LoginManager(application)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
application.jinja_env.filters['zip'] = zip


from app import database
from app import routes
from app.authentication.routes import authentication
from app.stories.routes import stories
from app.index.routes import index
from app.store.routes import store
from app.admin.routes import admin
from app.profile.routes import profile
from app.cart.routes import cart
from app.checkout.routes import checkout

application.register_blueprint(authentication)
application.register_blueprint(stories)
application.register_blueprint(index)
application.register_blueprint(store)
application.register_blueprint(admin)
application.register_blueprint(profile)
application.register_blueprint(cart)
application.register_blueprint(checkout)
