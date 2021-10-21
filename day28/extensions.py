from flask_sqlalchemy import SQLAlchemy
from app import app 
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy(app)             #app-i tanitmaq uchun 
migrate = Migrate(app, db)
login_manager = LoginManager(app)
