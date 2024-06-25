from flask import Blueprint
from flask import request
from app import db, bcrypt

subscriptions_bp = Blueprint("subscriptions", __name__, url_prefix='/subscriptions')

#create a new subscription
@subscriptions_bp.route("/", methods=["POST"])
def create_subscription():
    pass

#get subscription by ID
@subscriptions_bp.route("/<int:id>", methods=["GET"])
def get_subscription(id):
    pass

#get all subscriptions by user ID
@subscriptions_bp.route("/user/<int:id>", methods=["GET"])
def get_all_user_subscriptions(id):
    pass

#get all subscriptions
@subscriptions_bp.route("/", methods=["GET"])
def get_all_subscriptions():
    pass

#update a subscription by ID
@subscriptions_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_subscription(id):
    pass

#delete a subscription by ID
@subscriptions_bp.route("/<int:id>", methods=["DELETE"])
def delete_subscription():
    pass