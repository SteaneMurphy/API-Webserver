from flask import Blueprint
from flask import request
from app import db, bcrypt
from models.subscription import Subscription, SubscriptionSchema
from security.auth import admin_only, verify_admin
from flask_jwt_extended import jwt_required, get_jwt_identity

subscription_details_bp = Blueprint("subscription_details", __name__, url_prefix='/subscription-details')