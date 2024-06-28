from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models.user import User
from flask import abort, jsonify, make_response
import random

def admin_only(fn):
    @wraps(fn)
    @jwt_required()
    def inner(*args, **kwargs):
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id, User.admin)
        user = db.session.scalar(stmt)
        if user:
            return fn(*args, **kwargs)
        else:
            return {"error": "Unauthorised: Admin Only"}, 403
    return inner

def admin_or_owner(fn):
    @wraps(fn)
    @jwt_required()
    def inner(*args, **kwargs):
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id)
        user = db.session.scalar(stmt)

        if not user:
            abort(make_response(jsonify(error="User not found"), 404))
        if not user.admin and user_id != kwargs.get('id'):
            abort(make_response(jsonify(error="Unauthorised"), 403))

        return fn(*args, **kwargs)
    return inner

# Ensure that the JWT user is the owner of the account
@jwt_required()
def account_owner(id):
    user_id = get_jwt_identity()
    if user_id != id:
        abort(make_response(jsonify(error="Unauthorised"), 403))
    else:
        return True

@jwt_required()
def user_or_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).where(User.id == user_id)
    user = db.session.scalar(stmt)
    if user.admin:
        return "admin"
    elif user:
        return "user"

def generate_license():
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
               'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
               ',', '.', '<', '>', '/', '?', '{', '}', ':', ';']
    
    key = "#"
    for i in range(50):
        key += random.choice(symbols)

    return key