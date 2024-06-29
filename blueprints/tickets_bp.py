from flask import Blueprint
from flask import request
from app import db
from models.support_ticket import Ticket, TicketSchema
from security.auth import admin_only, admin_or_owner
from flask_jwt_extended import jwt_required, get_jwt_identity

#blueprint URI
tickets_bp = Blueprint("tickets", __name__, url_prefix='/tickets')



#create a new support ticket linked to a user ID (id: USER ID)
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



#return a support ticket by ticket ID (id: TICKET ID)
@tickets_bp.route("/<int:id>", methods=["GET"])
@admin_or_owner("ticket")
def get_ticket(id):
    #query database to find a ticket ID that matches ID sent in the header, otherwise return 404
    ticket = db.get_or_404(Ticket, id)
    return TicketSchema().dump(ticket)



#get all tickets linked to a user ID (id: USER ID)
@tickets_bp.route("/user/<int:id>", methods=["GET"])
@admin_or_owner("user")
def get_user_tickets(id):
    #returns all ticket entries from the 'tickets' database table that also have the supplied user ID foreign key
    #STATEMENT: SELECT tickets.id, tickets.issue_description, tickets.status, tickets.user_id 
    #           FROM tickets WHERE tickets.user_id = <request.id>
    stmt = db.select(Ticket).where(Ticket.user_id == id)
    tickets = db.session.scalars(stmt).all()
    return TicketSchema(many=True).dump(tickets)



#returns a list of all tickets in database
@tickets_bp.route("/", methods=["GET"])
@admin_only
def get_all_tickets():
    #returns a ticket object with all associated fields for each entry in the tickets table
    #STATEMENT: SELECT tickets.id, tickets.issue_description, tickets.status, tickets.user_id FROM tickets
    stmt = db.select(Ticket)
    tickets = db.session.scalars(stmt).all()
    return TicketSchema(many=True, unknown="exclude").dump(tickets)



#update a support ticket by ticket ID (id: TICKET ID)
@tickets_bp.route("/<int:id>", methods=["PUT", "PATCH"])
@admin_or_owner("ticket")
def update_ticket(id):
    #query database to find a ticket ID that matches ID sent in the header, otherwise return 404
    ticket = db.get_or_404(Ticket, id)
    #load schema and update fields with new data
    input_data = TicketSchema(unknown="exclude").load(request.json)
    ticket.issue_description = input_data.get("issue_description", ticket.issue_description)
    ticket.status = input_data.get("status", ticket.status)
    #commit changes to database
    db.session.commit()
    return TicketSchema().dump(ticket)



#delete a support ticket by ticket ID (id: TICKET ID)
@tickets_bp.route("/<int:id>", methods=["DELETE"])
@admin_only
def delete_ticket(id):
    #query database to find a ticket ID that matches ID sent in the header, otherwise return 404
    ticket = db.get_or_404(Ticket, id)
    db.session.delete(ticket)
    db.session.commit()
    return {}