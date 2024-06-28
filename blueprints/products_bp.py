from flask import Blueprint
from flask import request
from flask_jwt_extended import jwt_required
from app import db
from models.product import Product, ProductSchema
from security.auth import admin_only

#blueprint URI
products_bp = Blueprint("products", __name__, url_prefix='/products')



#create a new product
@products_bp.route("/", methods=["POST"])
@admin_only
def create_product():
    input_data = ProductSchema().load(request.json, unknown="exclude")
    new_product = Product(
        product_name=input_data["product_name"],
        description=input_data["description"]
    )
    db.session.add(new_product)
    db.session.commit()
    return ProductSchema().dump(new_product), 201



#get product by ID (id: PRODUCT ID)
@products_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_product(id):
    #query database to find a product ID that matches ID sent in the header, otherwise return 404
    product = db.get_or_404(Product, id)
    return ProductSchema().dump(product)



# #get all products by user ID - better suited for subscriptiondetails
# @products_bp.route("/user/<int:id>", methods=["GET"])
# def get_all_user_products(id):
#     stmt = db.select(Product).where(Ticket.user_id == id, user == id)
#     products = db.session.scalars(stmt).all()
#     return ProductSchema(many=True).dump(products)



#get all products in the database
@products_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_products():
    #query returns a product object with all associated fields for each entry in the products table
    # STATEMENT: SELECT products.id, products.product_name, products.description FROM products
    stmt = db.select(Product)
    products = db.session.scalars(stmt).all()
    return ProductSchema(many=True, unknown="exclude").dump(products)



#update a product by ID (id: PRODUCT ID)
@products_bp.route("/<int:id>", methods=["PUT", "PATCH"])
@admin_only
def update_product(id):
    #query database to find a product ID that matches ID sent in the header, otherwise return 404
    product = db.get_or_404(Product, id)
    
    input_data = ProductSchema(unknown="exclude").load(request.json)
    product.product_name = input_data.get("product_name", product.product_name)
    product.description = input_data.get("description", product.description)
    
    db.session.commit()
    return ProductSchema().dump(product)



#originally allowed for products to be deleted as per CRUD but realised that the database is not designed for such an endpoint. If a product
#is deleted, it will result in NULL fields in associated subscription_details table entries, the only solution to that, is that the entries cascade delete upto the 
#subscription table. This is not desired. Products can simply be updated or not offered for selection on the front-end.

# #delete a product by ID
# @products_bp.route("/<int:id>", methods=["DELETE"])
# def delete_product(id):
#     product = db.get_or_404(Product, id)
#     db.session.delete(product)
#     db.session.commit()
#     return {}