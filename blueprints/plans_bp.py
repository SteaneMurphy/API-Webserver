from datetime import timedelta
from flask import Blueprint, jsonify, abort, make_response
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt
from models.plan import Plan, PlanSchema
from models.subscription import Subscription
from security.auth import admin_only

plans_bp = Blueprint("plans", __name__, url_prefix='/plans')

#create a new plan
@plans_bp.route("/", methods=["POST"])
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

#get plan by ID
@plans_bp.route("/<int:id>", methods=["GET"])
def get_plan(id):
    plan = db.get_or_404(Plan, id)
    return PlanSchema().dump(plan)

#get all plans by user ID
@plans_bp.route("/user/<int:id>", methods=["GET"])
def get_all_user_plans(id):
    stmt = db.select(Plan).join(Subscription).where(Subscription.user_id == id)
    payments = db.session.scalars(stmt).all()
    return PlanSchema(many=True).dump(payments)

#get all plans
@plans_bp.route("/", methods=["GET"])
def get_all_plans():
    stmt = db.select(Plan)
    plans = db.session.scalars(stmt).all()
    return PlanSchema(many=True, unknown="exclude").dump(plans)

#update a plan by ID
@plans_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_plan(id):
    plan = db.get_or_404(Plan, id)
    input_data = PlanSchema(unknown="exclude").load(request.json)
    plan.plan_name = input_data.get("plan_name", plan.plan_name)
    plan.description = input_data.get("description", plan.description)
    plan.price = input_data.get("price", plan.price)
    plan.length = input_data.get("length", plan.length)
    plan.product_limit = input_data.get("product_limit", plan.product_limit)
    db.session.commit()
    return PlanSchema().dump(plan)

# #delete a plan by ID                                    - cant delete a plan because a subscription cant exist without a plan
# @plans_bp.route("/<int:id>", methods=["DELETE"])
# def delete_plan(id):
#     plan = db.get_or_404(Plan, id)
#     db.session.delete(plan)
#     db.session.commit()
#     return {}