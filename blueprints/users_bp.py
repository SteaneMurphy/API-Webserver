from datetime import timedelta
from flask import Blueprint, jsonify, abort, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt
from models.user import User, UserSchema
#from models.subscription import Subscription, SubscriptionSchema <- work on this feature later
from Security.auth import admin_only


users_bp = Blueprint("users", __name__, url_prefix='/users')

#create a new user account
@users_bp.route("/", methods=["POST"])
def create_user():
    input_data = UserSchema(only=["first_name", "last_name", "email", "password"]).load(request.json, unknown="exclude")
    
    #check if email already registered to an existing account
    stmt = db.select(User).where(User.email == input_data["email"])
    user = db.session.scalar(stmt)
    if user:
        return {"error":"Account already registered"}, 401
    
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
    login_data = UserSchema(only=["email", "password"]).load(request.json, unknown="exclude")

    # Compare email and password against db
    stmt = db.select(User).where(User.email == login_data["email"])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, login_data["password"]):
        # Generate the JWT
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        # Return the JWT
        return {"token": token}
    else:
        # Error handling (user not found, wrong username or wrong password)
        return {"error": "Invalid email or password"}, 401

#get user account by user ID, excludes password
@users_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_user(id):
    user_id = get_jwt_identity()
    print(user_id)
    user = db.get_or_404(User, id)
    return UserSchema(exclude=["password"]).dump(user)

#returns a list of all users in database + details (excl. password)
@users_bp.route("/", methods=["GET"])
def get_all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True, exclude=["password"]).dump(users)

# #returns a summary of linked tables by user ID, useful when looking up a user account
# @users_bp.route("/summary/<int:id>", methods=["GET"])
# def user_summary(id):
#     user = db.get_or_404(User, id)
#     subscriptons = db.select(Subscription).where(Subscription.user_id == user.id)
#     final = db.session.scalars(subscriptons).all()
#     return SubscriptionSchema(many=True, exclude=["user"]).dump(final)

#updates the name and email of an existing user account
@users_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_user(id):
    user = db.get_or_404(User, id)
    #auth owner or admin
    input_data = UserSchema(exclude=["password", "date_created", "last_login"], unknown="exclude").load(request.json)
    user.first_name = input_data.get("first_name", user.first_name)
    user.last_name = input_data.get("last_name", user.last_name)
    user.email = input_data.get("email", user.email)
    db.session.commit()
    return UserSchema(exclude=["password"]).dump(user)

#updates the password for the user account
@users_bp.route("/credentials/<int:id>", methods=["PUT", "PATCH"])
def change_user_password(id):
    user = db.get_or_404(User, id)
    new_password = UserSchema(only=["password"], unknown="exclude").load(request.json)
    user.password = bcrypt.generate_password_hash(new_password.get("password", user.password)).decode("utf8")
    db.session.commit()
    return UserSchema().dump(user)

#deletes an existing user account
@users_bp.route("/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = db.get_or_404(User, id)
    db.session.delete(user)
    db.session.commit()
    return {}