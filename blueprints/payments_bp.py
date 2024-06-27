from datetime import date
from flask import Blueprint, jsonify, abort, make_response
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt
from models.payment import Payment, PaymentSchema
from models.subscription import Subscription
from models.plan import Plan
from security.auth import admin_only
from flask_jwt_extended import jwt_required, get_jwt_identity

payments_bp = Blueprint("payments", __name__, url_prefix='/payments')

#create a new payment by subscription ID
@payments_bp.route("/<int:id>", methods=["POST"])
def create_payment(id):
    input_data = PaymentSchema().load(request.json, unknown="exclude")
    stmt = db.select(Subscription).where(Subscription.id == id)
    subscription = db.session.scalar(stmt)
    stmt2 = db.select(Plan).where(Plan.id == subscription.plan_id)
    plan = db.session.scalar(stmt2)
    new_ticket = Payment(
        amount=plan.price,
        payment_date=date.today(),
        payment_type=check_payment_type(plan.price, input_data["payment_type"]),
        subscription_id=id
    )
    db.session.add(new_ticket)
    db.session.commit()
    return PaymentSchema().dump(new_ticket), 201

def check_payment_type(price, payment_type):
    if price == 0.0:
        return "free"
    else:
        return payment_type

#get payment by payment ID
@payments_bp.route("/<int:id>", methods=["GET"])
def get_payment(id):
    payment = db.get_or_404(Payment, id)
    return PaymentSchema().dump(payment)

#get all payments by user ID
@payments_bp.route("/user/<int:id>", methods=["GET"])
def get_all_user_payments(id):
    stmt = db.select(Payment).join(Subscription).where(Subscription.user_id == id)
    payments = db.session.scalars(stmt).all()
    return PaymentSchema(many=True).dump(payments)

#get all payments
@payments_bp.route("/", methods=["GET"])
def get_all_payments():
    stmt = db.select(Payment)
    payments = db.session.scalars(stmt).all()
    return PaymentSchema(many=True).dump(payments)

#update a payment by payment ID
@payments_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_payment(id):
    payment = db.get_or_404(Payment, id)
    input_data = PaymentSchema(unknown="exclude").load(request.json)
    payment.amount = input_data.get("amount", payment.amount)
    payment.payment_type = input_data.get("payment_type", payment.payment_type)
    db.session.commit()
    return PaymentSchema().dump(payment)

#delete a payment by payment ID
@payments_bp.route("/<int:id>", methods=["DELETE"])
def delete_payment(id):
    payment = db.get_or_404(Payment, id)
    db.session.delete(payment)
    db.session.commit()
    return {}