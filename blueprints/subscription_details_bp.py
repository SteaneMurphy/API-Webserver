from flask import Blueprint
from app import db
from models.subscription_details import SubscriptionDetail, SubscriptionDetailSchema
from security.auth import admin_only, admin_or_owner

#blueprint URI
subscription_details_bp = Blueprint("subscription_details", __name__, url_prefix='/subscription-details')

#creation of new subscription_detail entries are tied to the creation of a new subscription and are handled by the 'create new subscription' endpoint,
#as this is just an association table

#deletion of subscription_detail entries are tied to the deletion of a subscription entry. When a subscription is deleted, all associated subscription_details are
#deleted by cascade. There is no reason to delete this entity whilst its associated subscription is still active



#get subscription_detail by ID (id: SUBSCRIPTION_DETAIL ID)
@subscription_details_bp.route("/<int:id>", methods=["GET"])
@admin_or_owner("subscription_detail")
def get_subscription_detail(id):
    #query database to find a subscription_detail ID that matches ID sent in the header, otherwise return 404 (get_or_404 method was bugged and not working??)
    subscription = db.session.query(SubscriptionDetail).get(id)
    if subscription is None:
        return{"error": "resource not found"}, 404
    
    return SubscriptionDetailSchema().dump(subscription)



#get subscription details by Subscription ID (id: SUBSCRIPTION ID)
@subscription_details_bp.route("/subscription/<int:id>", methods=["GET"])
@admin_or_owner("subscription")
def get_user_tickets(id):
    #query returns SubscriptionDetail object with all fields where it also contains the subscription ID sent in the header
    #STATEMENT: SELECT subscription_details.id, subscription_details.license, subscription_details.product_id, subscription_details.subscription_id 
    #           FROM subscription_details WHERE subscription_details.subscription_id = <request:id>
    stmt = db.select(SubscriptionDetail).where(SubscriptionDetail.subscription_id == id)
    details = db.session.scalars(stmt).all()
    print(stmt)
    return SubscriptionDetailSchema(many=True).dump(details)



#get all subscription details in database
@subscription_details_bp.route("/", methods=["GET"])
@admin_only
def get_all_tickets():
    #query returns all subscription_detail entries in the database
    #STATEMENT: SELECT subscription_details.id, subscription_details.license, subscription_details.product_id, subscription_details.subscription_id 
    #           FROM subscription_details
    stmt = db.select(SubscriptionDetail)
    details = db.session.scalars(stmt).all()
    print(stmt)
    return SubscriptionDetailSchema(many=True, unknown="exclude").dump(details)