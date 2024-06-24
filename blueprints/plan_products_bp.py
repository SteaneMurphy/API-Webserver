from datetime import timedelta
from flask import Blueprint, jsonify, abort, make_response
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt

plan_products_bp = Blueprint("plan_products", __name__, url_prefix='/plan_products')