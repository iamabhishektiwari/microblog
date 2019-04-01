from flask import Flask

from config import Config # configeration files
from flask_sqlalchemy import SQLAlchemy # for database handling
from flask_migrate import Migrate # Migrate tables to the database
from flask_login import LoginManager # Manages User login and logouts

#Initializzing flask app
app = Flask(__name__)

#Setting configeration file
app.config.from_object(Config)

#Setting database
db = SQLAlchemy(app)

#Setting for Migrations
migrate = Migrate(app,db)

#Setting loginmanager
login = LoginManager(app)

#Redirect for the pages where login is must.
login.login_view = 'login'

#routes contains views of each url
#models contains details of the table created in database.
from app import routes, models, error