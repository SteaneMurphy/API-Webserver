from flask import Blueprint
from flask import request
from app import db, bcrypt
from models.subscription import Subscription, SubscriptionSchema
from security.auth import admin_only, verify_admin
from flask_jwt_extended import jwt_required, get_jwt_identity

subscriptions_bp = Blueprint("subscriptions", __name__, url_prefix='/subscriptions')

#create a new subscription
@subscriptions_bp.route("/", methods=["POST"])
@jwt_required()
def create_subscription():
    input_data = SubscriptionSchema(exclude=["start_date", "end_date"]).load(request.json, unknown="exclude")
    user = get_jwt_identity()    
    new_subscription = Subscription(
        status = input_data["status"],
        user_id = user,
        plan_id = input_data["plan_id"]
    )
    db.session.add(new_subscription)
    db.session.commit()
    return SubscriptionSchema().dump(new_subscription), 201

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
@admin_only
def get_all_subscriptions():
    stmt = db.select(Subscription)
    subscriptions = db.session.scalars(stmt).all()
    return SubscriptionSchema(many=True, exclude=["plan"], unknown="exclude").dump(subscriptions)

#update a subscription by ID
@subscriptions_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_subscription(id):
    pass

#delete a subscription by ID
@subscriptions_bp.route("/<int:id>", methods=["DELETE"])
def delete_subscription():
    pass

# #returns a summary of linked tables by user ID, useful when looking up a user account
# @users_bp.route("/<int:id>/summary", methods=["GET"])
# def user_summary(id):
#     user = db.get_or_404(User, id)
#     subscriptons = db.select(Subscription).where(Subscription.user_id == user.id)
#     final = db.session.scalars(subscriptons).all()
#     return SubscriptionSchema(many=True, exclude=["user"]).dump(final)