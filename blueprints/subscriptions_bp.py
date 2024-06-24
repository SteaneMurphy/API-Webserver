from datetime import timedelta
from flask import Blueprint, jsonify, abort, make_response
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt

subscriptions_bp = Blueprint("subscriptions", __name__, url_prefix='/subscriptions')