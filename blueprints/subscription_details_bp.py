from flask import Blueprint
from flask import request
from app import db, bcrypt
from models.subscription_details import SubscriptionDetail, SubscriptionDetailSchema
from security.auth import admin_only, verify_admin,generate_license
from flask_jwt_extended import jwt_required, get_jwt_identity

subscription_details_bp = Blueprint("subscription_details", __name__, url_prefix='/subscription-details')

# #create a new subscription_detail
# @subscription_details_bp.route("/", methods=["POST"])
# def create_product():
#     input_data = SubscriptionDetailSchema().load(request.json, unknown="exclude")
#     new_subscription_detail = SubscriptionDetail(
#         license = generate_license(),
#         plan_id=,
#         product_id=,
#         subscription_id=
#     )
#     db.session.add(new_subscription_detail)
#     db.session.commit()
#     return SubscriptionDetailSchema().dump(new_subscription_detail), 201

#get subscription by ID
@subscription_details_bp.route("/<int:id>", methods=["GET"])
def get_subscription_detail(id):
    subscription = db.get_or_404(SubscriptionDetail, id)
    return SubscriptionDetailSchema().dump(subscription)

#get subscription details by Subscription ID
@subscription_details_bp.route("/subscription/<int:id>", methods=["GET"])
def get_user_tickets(id):
    stmt = db.select(SubscriptionDetail).where(SubscriptionDetail.subscription_id == id)
    details = db.session.scalars(stmt).all()
    return SubscriptionDetailSchema(many=True).dump(details)

#get all subscripton details
@subscription_details_bp.route("/", methods=["GET"])
def get_all_tickets():
    stmt = db.select(SubscriptionDetail)
    details = db.session.scalars(stmt).all()
    return SubscriptionDetailSchema(many=True, unknown="exclude").dump(details)

# #update a support ticket by ID  - complex
# @tickets_bp.route("/<int:id>", methods=["PUT", "PATCH"])
# def update_ticket(id):
#     ticket = db.get_or_404(Ticket, id)
#     input_data = TicketSchema(unknown="exclude").load(request.json)
#     ticket.issue_description = input_data.get("issue_description", ticket.issue_description)
#     ticket.status = input_data.get("status", ticket.status)
#     db.session.commit()
#     return TicketSchema().dump(ticket)

#delete a subscription details by ID        - is deleting plans and products, need to fix
@subscription_details_bp.route("/<int:id>", methods=["DELETE"])
def delete_ticket(id):
    details = db.get_or_404(SubscriptionDetail, id)
    db.session.delete(details)
    db.session.commit()
    return {}