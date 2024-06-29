from flask import Blueprint
from flask import request
from flask_jwt_extended import jwt_required
from app import db, bcrypt
from models.plan import Plan, PlanSchema
from models.subscription import Subscription
from security.auth import admin_only, admin_or_owner

#blueprint URI
plans_bp = Blueprint("plans", __name__, url_prefix='/plans')



#create a new plan
@plans_bp.route("/", methods=["POST"])
@admin_only
def create_plan():
    input_data = PlanSchema().load(request.json, unknown="exclude")
    new_plan = Plan(
        plan_name=input_data["plan_name"],
        description=input_data["description"],
        price=input_data["price"],
        length=input_data["length"],
        product_limit=input_data["product_limit"]
    )
    db.session.add(new_plan)
    db.session.commit()
    return PlanSchema().dump(new_plan), 201



#get plan by ID (id: PLAN ID)
@plans_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_plan(id):
    #query database to find a plan ID that matches ID sent in the header, otherwise return 404
    plan = db.get_or_404(Plan, id)
    return PlanSchema().dump(plan)



#get all plans by user ID (id: USER ID)
@plans_bp.route("/user/<int:id>", methods=["GET"])
@admin_or_owner("plan")
def get_all_user_plans(id):
    #this query joins a new table of Plan and Subscription fields for every plan listed by user id supplied in the header
    #for every plan linked to a subscription that is linked to the associated user id
    #STATEMENT: SELECT plans.id, plans.plan_name, plans.description, plans.price, plans.length, plans.product_limit 
    #           FROM plans JOIN subscriptions ON plans.id = subscriptions.plan_id WHERE subscriptions.user_id = <request:id>
    stmt = db.select(Plan).join(Subscription).where(Subscription.user_id == id)
    payments = db.session.scalars(stmt).all()
    return PlanSchema(many=True).dump(payments)



#returns a list of all plans in the database
@plans_bp.route("/", methods=["GET"])
@jwt_required
def get_all_plans():
    #query returns a plan object with all associated fields for each entry in the plans table
    #STATEMENT: SELECT plans.id, plans.plan_name, plans.description, plans.price, plans.length, plans.product_limit 
    #           FROM plans
    stmt = db.select(Plan)
    plans = db.session.scalars(stmt).all()
    return PlanSchema(many=True, unknown="exclude").dump(plans)



#update a plan by ID (id: PLAN ID)
@plans_bp.route("/<int:id>", methods=["PUT", "PATCH"])
@admin_only
def update_plan(id):
    #query database to find a plan ID that matches ID sent in the header, otherwise return 404
    plan = db.get_or_404(Plan, id)
    
    input_data = PlanSchema(unknown="exclude").load(request.json)
    plan.plan_name = input_data.get("plan_name", plan.plan_name)
    plan.description = input_data.get("description", plan.description)
    plan.price = input_data.get("price", plan.price)
    plan.length = input_data.get("length", plan.length)
    plan.product_limit = input_data.get("product_limit", plan.product_limit)
    
    db.session.commit()
    return PlanSchema().dump(plan)



#originally allowed for plans to be deleted as per CRUD but realised that the database is not designed for such an endpoint. If a plan
#is deleted, it will result in NULL fields in associated subscription table entries, the only solution to that, is that the subscription entry
#has to be deleted as well. A plan must therefore be updated rather than deleted unless all affected users are moved to a different plan before
#plan deletion. A user can delete their subscription from the subscription endpoint.

# #delete a plan by ID                                    
# @plans_bp.route("/<int:id>", methods=["DELETE"])
# def delete_plan(id):
#     plan = db.get_or_404(Plan, id)
#     db.session.delete(plan)
#     db.session.commit()
#     return {}