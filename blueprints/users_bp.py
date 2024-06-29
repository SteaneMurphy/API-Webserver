from datetime import date, timedelta
from flask import Blueprint
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt
from models.user import User, UserSchema
from security.auth import admin_only, admin_or_owner, user_or_admin
from sqlalchemy.orm import load_only

#blueprint URI
users_bp = Blueprint("users", __name__, url_prefix='/users')

#creates a new user account, admin role cannot be set here for security reasons
#returns new user details, excluding password or admin status for security reasons
@users_bp.route("/", methods=["POST"])
def create_user():
    input_data = UserSchema(only=["first_name", "last_name", "email", "password"]).load(request.json, unknown="exclude")
    
    #this query loads a user from the database if that user matches the email field submitted in the POST request. If the query finds a match
    #then it means this email has already been used to register an account and an error is returned. The query only returns a user object with id and email fields
    #STATEMENT: SELECT users.id, users.email FROM users WHERE users.email = <request.email>
    stmt = db.select(User).options(load_only(User.email)).where(User.email == input_data["email"])
    user = db.session.scalar(stmt)
    if user:
        return {"error":"account already exists under this email"}, 403
    
    new_user = User(
        first_name = input_data["first_name"],
        last_name = input_data["last_name"],
        email = input_data["email"],
        password = bcrypt.generate_password_hash(input_data["password"]).decode("utf8"),    #password is encrypted before storage into database
        date_created = date.today(),
        last_login = date.today()
    )
    db.session.add(new_user)
    db.session.commit()
    
    return UserSchema(exclude=["password", "admin"]).dump(new_user), 201                    #do not return password or admin status upon success



#login to existing user account using email and password
@users_bp.route("/login", methods=["POST"])
def login():
    #only use the email and password fields in POST request
    login_data = UserSchema(only=["email", "password", "last_login"]).load(request.json, unknown="exclude")

    #Query returns the entire user object (first_name, last_name, email, etc) when it finds a match on the supplied email from the POST request
    #STATMENT: SELECT users.id, users.first_name, users.last_name, users.email, users.password, users.admin, users.date_created, users.last_login 
    #FROM users WHERE users.email = <request.email>
    stmt = db.select(User).where(User.email == login_data["email"])
    user = db.session.scalar(stmt)

    #checks if user password matches password in database, generates session token upon success
    if user and bcrypt.check_password_hash(user.password, login_data["password"]):
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        user.last_login = date.today()
        db.session.commit()
        return {"token": token}
    else:
        return {"error": "email and/or password incorrect"}, 401



#get user account details by user ID (id: USER ID)
@users_bp.route("/<int:id>", methods=["GET"])
def get_user(id):
    #query database to find a user ID that matches ID sent in the header, otherwise return 404
    user = db.get_or_404(User, id)

    #tailor reponse depending on whether it is a user or admin requesting user details
    if user_or_admin() == "admin":
        return UserSchema(exclude=["password"]).dump(user)
    elif user_or_admin() == "user":
        return UserSchema(exclude=["password", "admin"]).dump(user)



#returns a list of all user account details for each user in database (excl. password)
@users_bp.route("/", methods=["GET"], endpoint="one")
@admin_only
def get_all_users():
    #returns a user object with all associated fields for each entry in the users table
    #STATEMENT: SELECT users.id, users.first_name, users.last_name, users.email, users.password, 
    #           users.admin, users.date_created, users.last_login FROM users
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    print(stmt)
    return UserSchema(many=True, exclude=["password"]).dump(users)



#set the admin role for a specific account by ID, admin cannot be set in account creation for security reasons (id: USER ID)
@users_bp.route("/admin/<int:id>", methods=["PUT", "PATCH"])
@admin_only
def update_admin(id):
    #gets the user object if there is a match with the supplied user id from the header
    user = db.get_or_404(User, id)
    input_data = UserSchema(only=["admin"], unknown="exclude").load(request.json)
    user.admin = input_data.get("admin", user.admin)
    
    db.session.commit()
    return UserSchema(exclude=["password", "admin"]).dump(user)



#updates the name and email of an existing user account (id: USER ID)
@users_bp.route("/<int:id>", methods=["PUT", "PATCH"])
@admin_or_owner("user")
def update_user(id):
    #gets the user object if there is a match with the supplied user id from the header
    user = db.get_or_404(User, id)

    input_data = UserSchema(exclude=["password", "date_created", "last_login"], unknown="exclude").load(request.json)
    user.first_name = input_data.get("first_name", user.first_name)
    user.last_name = input_data.get("last_name", user.last_name)
    user.email = input_data.get("email", user.email)

    db.session.commit()
    return UserSchema(exclude=["password", "admin"]).dump(user)



#updates the password for an existing user account (id: USER ID)
@users_bp.route("/credentials/<int:id>", methods=["PUT", "PATCH"])
@admin_or_owner("user")
def change_user_password(id):
    #gets the user object if there is a match with the supplied user id from the header
    user = db.get_or_404(User, id)
    new_password = UserSchema(only=["password"], unknown="exclude").load(request.json)
    user.password = bcrypt.generate_password_hash(new_password.get("password", user.password)).decode("utf8")
    
    db.session.commit()
    return UserSchema(exclude=["password", "admin"]).dump(user)



#deletes an existing user account and associated entries on related tables (id: USER ID)
@users_bp.route("/<int:id>", methods=["DELETE"], endpoint="two")
@admin_only
def delete_user(id):
    #gets the user object if there is a match with the supplied user id from the header
    user = db.get_or_404(User, id)
    db.session.delete(user)
    db.session.commit()
    return {}