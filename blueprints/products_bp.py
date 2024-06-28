from datetime import timedelta
from flask import Blueprint, jsonify, abort, make_response
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt
from models.product import Product, ProductSchema
from security.auth import admin_only

products_bp = Blueprint("products", __name__, url_prefix='/products')

#create a new product
@products_bp.route("/", methods=["POST"])
def create_product():
    input_data = ProductSchema().load(request.json, unknown="exclude")
    new_product = Product(
        product_name=input_data["product_name"],
        description=input_data["description"]
    )
    db.session.add(new_product)
    db.session.commit()
    return ProductSchema().dump(new_product), 201

#get product by ID
@products_bp.route("/<int:id>", methods=["GET"])
def get_product(id):
    product = db.get_or_404(Product, id)
    return ProductSchema().dump(product)

# #get all products by user ID - better suited for subscriptiondetails
# @products_bp.route("/user/<int:id>", methods=["GET"])
# def get_all_user_products(id):
#     stmt = db.select(Product).where(Ticket.user_id == id, user == id)
#     products = db.session.scalars(stmt).all()
#     return ProductSchema(many=True).dump(products)

#get all products
@products_bp.route("/", methods=["GET"])
def get_all_products():
    stmt = db.select(Product)
    products = db.session.scalars(stmt).all()
    return ProductSchema(many=True, unknown="exclude").dump(products)

#update a product by ID
@products_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_product(id):
    product = db.get_or_404(Product, id)
    input_data = ProductSchema(unknown="exclude").load(request.json)
    product.product_name = input_data.get("product_name", product.product_name)
    product.description = input_data.get("description", product.description)
    db.session.commit()
    return ProductSchema().dump(product)

# #delete a product by ID   - cant only be deleted by cascade from association table
# @products_bp.route("/<int:id>", methods=["DELETE"])
# def delete_product(id):
#     product = db.get_or_404(Product, id)
#     db.session.delete(product)
#     db.session.commit()
#     return {}