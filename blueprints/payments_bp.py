from datetime import timedelta
from flask import Blueprint, jsonify, abort, make_response
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt

payments_bp = Blueprint("payments", __name__, url_prefix='/payments')