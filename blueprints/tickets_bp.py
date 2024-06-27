from datetime import date
from flask import Blueprint, jsonify, abort, make_response
from flask import request
from flask_jwt_extended import create_access_token
from app import db, bcrypt
from models.support_ticket import Ticket, TicketSchema
from security.auth import admin_only
from flask_jwt_extended import jwt_required, get_jwt_identity

tickets_bp = Blueprint("tickets", __name__, url_prefix='/tickets')

#create a support ticket
@tickets_bp.route("/", methods=["POST"])
@jwt_required()
def create_ticket():
    input_data = TicketSchema(exclude=["date_created"]).load(request.json, unknown="exclude")
    user = get_jwt_identity()
    new_ticket = Ticket(
        issue_description = input_data["issue_description"],
        status = input_data["status"],
        user_id = user
    )
    db.session.add(new_ticket)
    db.session.commit()
    return TicketSchema().dump(new_ticket), 201

#get support ticket by ID
@tickets_bp.route("/<int:id>", methods=["GET"])
def get_ticket(id):
    ticket = db.get_or_404(Ticket, id)
    return TicketSchema().dump(ticket)

#get all user tickets by user ID
@tickets_bp.route("/user/<int:id>", methods=["GET"])
def get_user_tickets():
    pass

#get all tickets
@tickets_bp.route("/", methods=["GET"])
def get_all_tickets():
    stmt = db.select(Ticket)
    tickets = db.session.scalars(stmt).all()
    return TicketSchema(many=True, unknown="exclude").dump(tickets)

#update a support ticket by ID
@tickets_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_ticket(id):
    ticket = db.get_or_404(Ticket, id)
    input_data = TicketSchema(unknown="exclude").load(request.json)
    ticket.issue_description = input_data.get("issue_description", ticket.issue_description)
    ticket.status = input_data.get("status", ticket.status)
    db.session.commit()
    return TicketSchema().dump(ticket)

#delete a support ticket
@tickets_bp.route("/<int:id>", methods=["DELETE"])
def delete_ticket(id):
    ticket = db.get_or_404(Ticket, id)
    db.session.delete(ticket)
    db.session.commit()
    return {}