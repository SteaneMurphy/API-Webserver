from datetime import timedelta
from flask import Blueprint, jsonify, abort, make_response
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt

payments_bp = Blueprint("payments", __name__, url_prefix='/payments')

#create a new payment
@payments_bp.route("/", methods=["POST"])
def create_payment():
    pass

#get payment by ID
@payments_bp.route("/<int:id>", methods=["GET"])
def get_payment(id):
    pass

#get all payments by user ID
@payments_bp.route("/user/<int:id>", methods=["GET"])
def get_all_user_payments(id):
    pass

#get all payments
@payments_bp.route("/", methods=["GET"])
def get_all_payments():
    pass

#update a payment by ID
@payments_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_payment(id):
    pass

#delete a payment by ID
@payments_bp.route("/<int:id>", methods=["DELETE"])
def delete_payment():
    pass