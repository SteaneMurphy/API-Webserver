from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models.user import User
from flask import abort, jsonify, make_response
import random

def admin_only(fn):
    @jwt_required()
    def inner():
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id, User.admin)
        user = db.session.scalar(stmt)
        if user:
            return fn()
        else:
            return {"error": "Unauthorised: Admin Only"}, 403
    return inner

@jwt_required()
def verify_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).where(User.id == user_id, User.admin)
    user = db.session.scalar(stmt)
    if user:
        return True
    else:
        return {"error": "You must be an admin"}, 403

# Ensure that the JWT user is the owner of the account
@jwt_required()
def account_owner(id):
    user_id = get_jwt_identity()
    if user_id != id:
        abort(make_response(jsonify(error="Unauthorised"), 403))
    else:
        return True
    
def generate_license():
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
               'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
               ',', '.', '<', '>', '/', '?', '{', '}', ':', ';']
    
    key = "#"
    for i in range(50):
        key += random.choice(symbols)

    return key