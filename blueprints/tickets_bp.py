from datetime import timedelta
from flask import Blueprint, jsonify, abort, make_response
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt

tickets_bp = Blueprint("tickets", __name__, url_prefix='/tickets')

#create a support ticket
@tickets_bp.route("/", methods=["POST"])
def create_ticket():
    pass

#get support ticket by ID
@tickets_bp.route("/<int:id>", methods=["GET"])
def get_ticket():
    pass

#get all user tickets by user ID
@tickets_bp.route("/user/<int:id>", methods=["GET"])
def get_user_tickets():
    pass

#get all tickets
@tickets_bp.route("/", methods=["GET"])
def get_all_tickets():
    pass

#update a support ticket by ID
@tickets_bp.route("/", methods=["PUT", "PATCH"])
def update_ticket():
    pass

#delete a support ticket
@tickets_bp.route("/<int:id>", methods=["DELETE"])
def delete_ticket():
    pass