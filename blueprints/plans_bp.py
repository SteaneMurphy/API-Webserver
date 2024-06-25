from datetime import timedelta
from flask import Blueprint, jsonify, abort, make_response
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt

plans_bp = Blueprint("plans", __name__, url_prefix='/plans')

#create a new plan
@plans_bp.route("/", methods=["POST"])
def create_plan():
    pass

#get plan by ID
@plans_bp.route("/<int:id>", methods=["GET"])
def get_plan(id):
    pass

#get all plans by user ID
@plans_bp.route("/user/<int:id>", methods=["GET"])
def get_all_user_plans(id):
    pass

#get all plans
@plans_bp.route("/", methods=["GET"])
def get_all_plans():
    pass

#update a plan by ID
@plans_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_plan(id):
    pass

#delete a plan by ID
@plans_bp.route("/<int:id>", methods=["DELETE"])
def delete_plan():
    pass