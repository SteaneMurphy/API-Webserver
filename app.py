from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

#allows SQLAlchemy to use its own types
class Base(DeclarativeBase):
    pass

#create a new Flask instance
app = Flask(__name__)

#get JWT secret key and databse URI from environment file (.env) -> dev user must set for their own environment, production will use their own values
app.config["JWT_SECRET_KEY"] = environ.get("JWT_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")

#create database instance and link to SQLAlchemy
db = SQLAlchemy(model_class=Base)
#initialise the database instance to the Flask application
db.init_app(app)
#create new instances of Marshmallow, Bcrypt and JWT and link to the Flask application
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp
app.register_blueprint(db_commands)
app.register_blueprint(users_bp)

