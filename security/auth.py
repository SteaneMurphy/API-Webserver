from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models.user import User
from models.support_ticket import Ticket
from models.subscription import Subscription
from models.payment import Payment
from models.subscription_details import SubscriptionDetail 
from flask import abort, jsonify, make_response
import random

#wrapped function decorator check if current JWT user is marked as admin in the database
def admin_only(fn):
    @wraps(fn)
    @jwt_required()
    def inner(*args, **kwargs):
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id, User.admin)
        user = db.session.scalar(stmt)
        if user:
            return fn(*args, **kwargs)
        else:
            return {"error": "Unauthorised: Admin Only"}, 403
    return inner

#wrapped decorator function checks if current JWT user accessing the resource is an admin or is the owner of said resource
def admin_or_owner(type):
    def outer(fn):
        @wraps(fn)
        @jwt_required()
        def inner(id, *args, **kwargs):
            #load JWT user
            user_id = get_jwt_identity()
            stmt = db.select(User).where(User.id == user_id)
            user = db.session.scalar(stmt)

            #if owner of resource
            try:
                if check_resource_owner(type, id).id == user_id:
                    return fn(id, *args, **kwargs)
            except:
                abort(make_response(jsonify(error="resource not found"), 404))
            #else if admin
            if user.admin:
                return fn(id, *args, **kwargs)
            else:
                #return error
                abort(make_response(jsonify(error="not authorised to access this resource"), 403))        
        return inner
    return outer

#helper function to determine which resource is being accessed
@jwt_required()
def check_resource_owner(type, id):
    match type:
        case "user":
            #queries the database to find a user id that matches the id sent into the function
            stmt = db.select(User).where(User.id == id)
            user = db.session.scalar(stmt)
            return user
        case "ticket":
            #queries the database by joining the ticket and user tables to find a user id that matches a ticket id that matches the id sent into the function
            stmt = db.select(User).join(Ticket, User.id == Ticket.user_id).where(Ticket.id == id)
            user = db.session.scalar(stmt)
            return user
        case "subscription":
            #queries the database by joining the subscription and user tables to find a match on the user id where the subscription id matches with the supplied function id
            stmt = db.select(User).join(Subscription, User.id == Subscription.user_id).where(Subscription.id == id)
            user = db.session.scalar(stmt)
            return user
        case "product":
            #queries the database by joining the user, subscription and subscription details tables by finding a user id match when subscription_detail id matches a product id
            stmt = db.select(User).join(Subscription, User.id == Subscription.user_id).join(SubscriptionDetail, Subscription.id == SubscriptionDetail.subscription_id).where(SubscriptionDetail.product_id == id)
            user = db.session.scalar(stmt)
            return user
        case "plan":
            #queries the database by joining the subscription and user tables to find a match on when the subscription id matches a plan id
            stmt = db.select(User).join(Subscription, User.id == Subscription.user_id).where(Subscription.plan_id == id)
            user = db.session.scalar(stmt)
            return user
        case "payment":
            #queries the database by joining the subscription, user and payment tables. Finds a user id by matching the payment id with the supplied function id
            stmt = db.select(User).join(Subscription, User.id == Subscription.user_id).join(Payment, Subscription.id == Payment.subscription_id).where(Payment.id == id)
            user = db.session.scalar(stmt)
            return user
        case "subscription_detail":
            #queries the database by joining the subscription, user and subscription tables. Finds a user id when there is a match on subscription_detail.subscription id with the supplied function id
            stmt = db.select(User).join(Subscription, User.id == Subscription.user_id).join(SubscriptionDetail, Subscription.id == SubscriptionDetail.subscription_id).where(SubscriptionDetail.subscription_id == id)
            user = db.session.scalar(stmt)
            return user
        case _:
            print("error")

# Ensure that the JWT user is the owner of the account
@jwt_required()
def account_owner(id):
    user_id = get_jwt_identity()
    if user_id != id:
        abort(make_response(jsonify(error="Unauthorised"), 403))
    else:
        return True

#generates a mock licence when a new product is registered in a new subscription
def generate_license():
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
               'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
               ',', '.', '<', '>', '/', '?', '{', '}', ':', ';']
    
    key = "#"
    for i in range(50):
        key += random.choice(symbols)

    return key