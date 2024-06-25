from datetime import timedelta
from flask import Blueprint, jsonify, abort, make_response
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt

plan_products_bp = Blueprint("plan_products", __name__, url_prefix='/plan_products')

#create a new plan_product
@plan_products_bp.route("/", methods=["POST"])
def create_plan_product():
    pass

#get plan_product by ID
@plan_products_bp.route("/<int:id>", methods=["GET"])
def get_plan_product(id):
    pass

#get all plan_products by user ID
@plan_products_bp.route("/user/<int:id>", methods=["GET"])
def get_all_user_plan_products(id):
    pass

#get all plan_products
@plan_products_bp.route("/", methods=["GET"])
def get_all_plan_products():
    pass

#update a plan_product by ID
@plan_products_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_plan_product(id):
    pass

#delete a plan_product by ID
@plan_products_bp.route("/<int:id>", methods=["DELETE"])
def delete_plan_product():
    pass