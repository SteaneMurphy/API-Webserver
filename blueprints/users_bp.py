from datetime import timedelta
from flask import Blueprint
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt
from models.user import User, UserSchema

users_bp = Blueprint("users", __name__, url_prefix='/users')

#create a new user account
@users_bp.route("/", methods=["POST"])
def create_user():
    input_data = UserSchema(only=["first_name", "last_name", "email", "password"]).load(request.json, unknown="exclude")
    new_user = User(
        first_name = input_data["first_name"],
        last_name = input_data["last_name"],
        email = input_data["email"],
        password = bcrypt.generate_password_hash(input_data["password"]).decode("utf8"),
    )
    db.session.add(new_user)
    db.session.commit()
    return UserSchema().dump(new_user), 201

#user login to existing account
@users_bp.route("/login", methods=["POST"])
def login():
    # Get the email and password from the request
    params = UserSchema(only=["email", "password"]).load(
        request.json, unknown="exclude"
    )
    # email = request.json['email']
    # password = request.json['password']
    # {email, password} = request.json
    # Compare email and password against db
    stmt = db.select(User).where(User.email == params["email"])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, params["password"]):
        # Generate the JWT
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        # Return the JWT
        return {"token": token}
    else:
        # Error handling (user not found, wrong username or wrong password)
        return {"error": "Invalid email or password"}, 401
