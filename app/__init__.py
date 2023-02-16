import logging

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

app = Flask(__name__)
app.static_folder = 'static'
app.config['SECRET_KEY'] = 'changethis'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

csrf = CSRFProtect(app)
Bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
log = logging.getLogger('werkzeug')
log.disabled = False

def load_routes():
    from app import routes


load_routes()
