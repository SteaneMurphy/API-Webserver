from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models.user import User
from flask import abort, jsonify, make_response


# Route decorator - ensure JWT user is an admin
@jwt_required()
def admin_only():
    user_id = get_jwt_identity()
    stmt = db.select(User).where(User.id == user_id, User.is_admin)
    user = db.session.scalar(stmt)
    if user:
        return True
    else:
        return {"error": "You do not posssess the privileges to access this resource"}, 403


# Ensure that the JWT user is the owner of the account
@jwt_required()
def verify_account_owner(obj):
    user_id = get_jwt_identity()
    if user_id != obj.user_id:
        abort(make_response(jsonify(error="You must be the account owner to access this resource"), 403))