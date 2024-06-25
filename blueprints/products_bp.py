from datetime import timedelta
from flask import Blueprint, jsonify, abort, make_response
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt

products_bp = Blueprint("products", __name__, url_prefix='/products')

#create a new product
@products_bp.route("/", methods=["POST"])
def create_product():
    pass

#get product by ID
@products_bp.route("/<int:id>", methods=["GET"])
def get_product(id):
    pass

#get all products by user ID
@products_bp.route("/user/<int:id>", methods=["GET"])
def get_all_user_products(id):
    pass

#get all products
@products_bp.route("/", methods=["GET"])
def get_all_products():
    pass

#update a product by ID
@products_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_product(id):
    pass

#delete a product by ID
@products_bp.route("/<int:id>", methods=["DELETE"])
def delete_product():
    pass