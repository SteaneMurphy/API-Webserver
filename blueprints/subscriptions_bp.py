from flask import Blueprint
from flask import request
from app import db, bcrypt
from models.subscription import Subscription, SubscriptionSchema
from security.auth import admin_only
from flask_jwt_extended import jwt_required, get_jwt_identity

subscriptions_bp = Blueprint("subscriptions", __name__, url_prefix='/subscriptions')

#create a new subscription - requires a plan, and product or else will not enter db properly - how to do?
@subscriptions_bp.route("/", methods=["POST"])
@jwt_required()
def create_subscription():
    input_data = SubscriptionSchema(exclude=["start_date", "end_date"]).load(request.json, unknown="exclude")
    user = get_jwt_identity()    
    new_subscription = Subscription(
        status = input_data["status"],
        user_id = user,
        plan_id = input_data["plan"]
    )
    db.session.add(new_subscription)
    db.session.commit()
    return SubscriptionSchema().dump(new_subscription), 201



#get subscription by ID
@subscriptions_bp.route("/<int:id>", methods=["GET"])
def get_subscription(id):
    subscription = db.get_or_404(Subscription, id)
    return SubscriptionSchema().dump(subscription)



#get all subscriptions by user ID
@subscriptions_bp.route("/user/<int:id>", methods=["GET"])
def get_all_user_subscriptions(id):
    stmt = db.select(Subscription).where(Subscription.user_id == id)
    subscriptions = db.session.scalars(stmt).all()
    return SubscriptionSchema(many=True).dump(subscriptions)



#get all subscriptions
@subscriptions_bp.route("/", methods=["GET"])
def get_all_subscriptions():
    stmt = db.select(Subscription)
    subscriptions = db.session.scalars(stmt).all()
    return SubscriptionSchema(many=True, exclude=["plan"], unknown="exclude").dump(subscriptions)



#update a subscription by ID - might need to update plan?
@subscriptions_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_subscription(id):
    subscription = db.get_or_404(Subscription, id)
    input_data = SubscriptionSchema(unknown="exclude").load(request.json)
    subscription.status = input_data.get("status", subscription.status)
    db.session.commit()
    return SubscriptionSchema().dump(subscription)



# #delete a subscription by ID - cant delete due to association table, must delete there
# @subscriptions_bp.route("/<int:id>", methods=["DELETE"])
# def delete_subscription(id):
#     subscription = db.get_or_404(Subscription, id)
#     db.session.delete(subscription)
#     db.session.commit()
#     return {}



# #returns a summary of linked tables by user ID, useful when looking up a user account
# @users_bp.route("/<int:id>/summary", methods=["GET"])
# def user_summary(id):
#     user = db.get_or_404(User, id)
#     subscriptons = db.select(Subscription).where(Subscription.user_id == user.id)
#     final = db.session.scalars(subscriptons).all()
#     return SubscriptionSchema(many=True, exclude=["user"]).dump(final)