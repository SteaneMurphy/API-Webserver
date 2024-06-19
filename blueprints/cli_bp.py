from flask import Blueprint
from app import db

db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def database_create():
    db.drop_all()
    db.create_all()
    print("Created tables")