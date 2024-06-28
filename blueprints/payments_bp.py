from datetime import date
from flask import Blueprint
from flask import request
from app import db, bcrypt
from models.payment import Payment, PaymentSchema
from models.subscription import Subscription
from models.plan import Plan
from security.auth import admin_only, admin_or_owner

#blueprint URI
payments_bp = Blueprint("payments", __name__, url_prefix='/payments')



#allows admin/system to add a payment to a subscription by a subscription ID (id: SUBSCRIPTION ID)
#this endpoint would be called by payment processing on the front-end to update a successful payment
#not a manual update method for the user to access
@payments_bp.route("/<int:id>", methods=["POST"])
@admin_only
def create_payment(id):
    input_data = PaymentSchema().load(request.json, unknown="exclude")
    
    #this query creates a join table of subscription and plan fields (listed below). The query loads the plan ID that is linked to the subscription ID
    #as per the id sent in the header and join their respective tables on the fields listed. This join is neccessary to find the price of the associated
    #plan used for this subscription

    #STATMENT: SELECT subscriptions.id, subscriptions.status, subscriptions.user_id, subscriptions.plan_id, plans.id AS id_1, plans.plan_name, 
    #           plans.description, plans.price, plans.length, plans.product_limit FROM subscriptions JOIN plans ON subscriptions.plan_id = plans.id 
    #           WHERE subscriptions.id = <request:id>
    stmt = db.select(Subscription, Plan).join(Plan, Subscription.plan_id == Plan.id).where(Subscription.id == id)    
    object = db.session.scalar(stmt)
    new_ticket = Payment(
        amount=object.plan.price,
        payment_date=date.today(),
        payment_type=check_payment_type(object.plan.price, input_data["payment_type"]),
        subscription_id=id
    )
    db.session.add(new_ticket)
    db.session.commit()
    return PaymentSchema().dump(new_ticket), 201
#automatically sets the payment type to 'free' if the user is on the 'free' plan
def check_payment_type(price, payment_type):
    if price == 0.0:
        return "free"
    else:
        return payment_type


#FIX BUGGED
#returns a payment by payment ID (id: PAYMENT ID)
@payments_bp.route("/<int:id>", methods=["GET"])
@admin_or_owner
def get_payment(id):
    #query database to find a payment ID that matches ID sent in the header, otherwise return 404
    payment = db.get_or_404(Payment, id)
    return PaymentSchema().dump(payment)


#FIX BUGGED
#returns all payments by user ID (id: USER ID)
@payments_bp.route("/user/<int:id>", methods=["GET"])
#@admin_or_owner
def get_all_user_payments(id):
    #this query joins entries from the payments table with entries from the subscription table that match the user ID (id: USER ID)
    #STATEMENT: SELECT payments.id, payments.amount, payments.payment_type, payments.subscription_id FROM payments 
    #           JOIN subscriptions ON subscriptions.id = payments.subscription_id WHERE subscriptions.user_id = <request:id>
    stmt = db.select(Payment).join(Subscription).where(Subscription.user_id == id)
    payments = db.session.scalars(stmt).all()
    return PaymentSchema(many=True).dump(payments)



#returns a list of all payments in database
@payments_bp.route("/", methods=["GET"])
@admin_only
def get_all_payments():
    #returns a payment object with all associated fields for each entry in the payments table
    #STATEMENT: SELECT payments.id, payments.amount, payments.payment_type, payments.subscription_id FROM payments
    stmt = db.select(Payment)
    payments = db.session.scalars(stmt).all()
    return PaymentSchema(many=True).dump(payments)



#update a payment by payment ID
@payments_bp.route("/<int:id>", methods=["PUT", "PATCH"])
@admin_only
def update_payment(id):
    #query database to find a payment ID that matches ID sent in the header, otherwise return 404
    payment = db.get_or_404(Payment, id)
    
    input_data = PaymentSchema(unknown="exclude").load(request.json)
    payment.amount = input_data.get("amount", payment.amount)
    payment.payment_type = input_data.get("payment_type", payment.payment_type)
    
    db.session.commit()
    return PaymentSchema().dump(payment)



#delete a payment by payment ID
@payments_bp.route("/<int:id>", methods=["DELETE"])
@admin_only
def delete_payment(id):
    #query database to find a payment ID that matches ID sent in the header, otherwise return 404
    payment = db.get_or_404(Payment, id)
    db.session.delete(payment)
    db.session.commit()
    return {}