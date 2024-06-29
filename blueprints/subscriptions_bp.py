from flask import Blueprint
from flask import request
from app import db
from models.subscription import Subscription, SubscriptionSchema
from models.plan import Plan
from models.subscription_details import SubscriptionDetail
from models.product import Product
from security.auth import admin_only, admin_or_owner, generate_license
from flask_jwt_extended import jwt_required, get_jwt_identity

#blueprint URI
subscriptions_bp = Blueprint("subscriptions", __name__, url_prefix='/subscriptions')

#create a new subscription - by creating a new subscription, this endpoint will automatically create new subscription_detail entries and associate
#a subscription_FK into the plans and subscription_details tables
#request body must include a valid plan ID and a list of valid product IDs 
@subscriptions_bp.route("/", methods=["POST"])
@jwt_required()
def create_subscription():
    input_data = SubscriptionSchema(exclude=["start_date", "end_date"]).load(request.json, unknown="exclude")
    
    #determine the plan object from the plan ID sent in the request
    #determine the product amount based on plan ID
    #STATEMENT: SELECT plans.id, plans.plan_name, plans.description, plans.price, plans.length, plans.product_limit 
    #           FROM plans WHERE plans.id = <input_data.plan_id>
    stmt = db.select(Plan).where(Plan.id == input_data["plan_id"])
    plan = db.session.scalar(stmt)
    print(stmt)
    product_limit = plan.product_limit

    #load a list of all plans in the database for later comparison
    #STATEMENT: SELECT plans.id, plans.plan_name, plans.description, plans.price, plans.length, plans.product_limit 
    #           FROM plans
    stmt2 = db.select(Plan)
    plans = db.session.scalars(stmt2).all()
    print(stmt2)

    #load a list of products in the database for later comparison
    #STATEMENT: SELECT products.id, products.product_name, products.description FROM products
    stmt3 = db.select(Product)
    products = db.session.scalars(stmt3).all()
    print(stmt3)

    #check that plans and products in request meet requirements
    if input_data["plan_id"] > len(plans):
        return { "error": "plan does not exist" }
    if len(input_data["products"]) > product_limit:
        return { "error": "too many products selected" }
    for i in input_data["products"]:
        if i > len(products):
            return { "error": "product doesn't exist" }
    
    #create new subscription
    user = get_jwt_identity()    
    new_subscription = Subscription(
        status = input_data["status"],
        user_id = user,
        plan_id = input_data["plan_id"]
    )
    db.session.add(new_subscription)
    #temp commit the new subscription so that the subscription_detail entries can reference the subscription_id
    db.session.flush()

    #for each product, generate a new subscription_detail and product license
    sub_details = []
    for i in input_data["products"]:
        print(i)
        sub_details.append(SubscriptionDetail(
            license = generate_license(),
            product_id = i,
            subscription_id = new_subscription.id
        ))

    db.session.add_all(sub_details)
    db.session.commit()
    return SubscriptionSchema(exclude=["user"]).dump(new_subscription), 201



#get subscription by ID (id: SUBSCRIPTION ID)
@subscriptions_bp.route("/<int:id>", methods=["GET"])
@admin_or_owner("subscription")
def get_subscription(id):
    #query database to find a subscription ID that matches ID sent in the header, otherwise return 404
    subscription = db.get_or_404(Subscription, id)
    return SubscriptionSchema().dump(subscription)



#get all subscriptions by user ID (id: USER ID)
@subscriptions_bp.route("/user/<int:id>", methods=["GET"])
@admin_or_owner("user")
def get_all_user_subscriptions(id):
    #returns a user object for a user entry on the users table that matches the user ID submitted in the header
    #STATEMENT: SELECT subscriptions.id, subscriptions.status, subscriptions.user_id, subscriptions.plan_id 
    #           FROM subscriptions WHERE subscriptions.user_id = <request:id>
    stmt = db.select(Subscription).where(Subscription.user_id == id)
    subscriptions = db.session.scalars(stmt).all()
    return SubscriptionSchema(many=True).dump(subscriptions)



#get all subscriptions
@subscriptions_bp.route("/", methods=["GET"])
@admin_only
def get_all_subscriptions():
    #returns a subscription object with all associated fields for each entry in the subscriptions table
    #STATEMENT: SELECT subscriptions.id, subscriptions.status, subscriptions.user_id, subscriptions.plan_id 
    #           FROM subscriptions
    stmt = db.select(Subscription)
    subscriptions = db.session.scalars(stmt).all()
    return SubscriptionSchema(many=True, exclude=["plan"], unknown="exclude").dump(subscriptions)



#update a subscription by ID (id: SUBSCRIPTION ID)
@subscriptions_bp.route("/<int:id>", methods=["PUT", "PATCH"])
@admin_only
def update_subscription(id):
    #query database to find a subscription ID that matches ID sent in the header, otherwise return 404
    subscription = db.get_or_404(Subscription, id)
    
    input_data = SubscriptionSchema(unknown="exclude").load(request.json)
    subscription.status = input_data.get("status", subscription.status)
    
    db.session.commit()
    return SubscriptionSchema(only=["id", "status", "user"]).dump(subscription)



#delete a subscription by subscription ID (id: SUBSCRIPTION ID)
@subscriptions_bp.route("/<int:id>", methods=["DELETE"])
@admin_only
def delete_subscription(id):
    #query database to find a subscription ID that matches ID sent in the header, otherwise return 404
    subscription = db.get_or_404(Subscription, id)
    db.session.delete(subscription)
    db.session.commit()
    return {}