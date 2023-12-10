from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

#TEMPLATE_DIR = os.path.abspath('templates')
#STATIC_DIR = os.path.abspath('static')
#app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'd26eae7e94a894cd29be700b1b06acef'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # to redirect to login page from login_required incase not logged in we are proving login funtion name
login_manager.login_message_category = 'info' # to change the color of the message to info'

from flaskblog import routes