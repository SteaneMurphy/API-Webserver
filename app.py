from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from marshmallow.exceptions import ValidationError

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

#blueprint registration area
from blueprints.cli_bp import cli_commands
from blueprints.users_bp import users_bp
from blueprints.tickets_bp import tickets_bp
from blueprints.payments_bp import payments_bp
from blueprints.subscription_details_bp import subscription_details_bp
from blueprints.plans_bp import plans_bp
from blueprints.subscriptions_bp import subscriptions_bp
from blueprints.products_bp import products_bp
app.register_blueprint(cli_commands)
app.register_blueprint(users_bp)
app.register_blueprint(tickets_bp)
app.register_blueprint(payments_bp)
app.register_blueprint(subscription_details_bp)
app.register_blueprint(plans_bp)
app.register_blueprint(subscriptions_bp)
app.register_blueprint(products_bp)

#home route
@app.route("/")
def index():
    return "Welcome to your SaaS API!"

#various error handling for HTTPS error codes
@app.errorhandler(405)
@app.errorhandler(404)
def resource_not_found(self):
    return { "error": "Resource not found" }, 404

@app.errorhandler(400)
def bad_request(self):
    return { "error": "bad request: body missing information" }, 400

@app.errorhandler(403)
@app.errorhandler(401)
def unauthorised():
    return { "error": "not authorised to access this resource" }, 401

@app.errorhandler(ValueError)
def invalid_request(err):
    return { "error": "field missing information" }, 500

@app.errorhandler(ValidationError)
def invalid_request(err):
    return { "error": vars(err)["messages"] }

@app.errorhandler(KeyError)
def invalid_request(err):
    return { "error": f"Missing field: {str(err)}" }, 400

@app.errorhandler(TypeError)
def invalid_request(err):
    return { "error": f"Type expected: {str(err)}" }

print(app.url_map)

