from datetime import date
from flask import Blueprint
from models.user import User
from models.subscription import Subscription
from models.payment import Payment
from models.support_ticket import Ticket
from models.plan import Plan
from models.product import Product
from models.plan_product import PlanProduct
from app import db
import json

db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def database_create():
    db.drop_all()
    db.create_all()
    print("Created tables")
    
    #four types of plans
    plans = [
        Plan(
            plan_name="Free",
            description="Access to service is free, can use upto 2 products",
            price=0,
            length=1000,
        ),
        Plan(
            plan_name="Basic",
            description="Provides basic access to service, comes with use of 4 products",
            price=15.99,
            length=30,
        ),
        Plan(
            plan_name="Advanced",
            description="Provides advanced access to service, comes with use of 5 products",
            price=29.99,
            length=30,
        ),
        Plan(
            plan_name="Pro",
            description="Provides professional access to service, comes with use of 6 products",
            price=49.99,
            length=30,
        ),
    ]

    db.session.add_all(plans)
    db.session.commit()

    users = []

    with open("seed_data/dummy_users.json") as f:
        data = json.load(f)
        for i in data:
            newUser = User()
            newUser.first_name = i['first_name']
            newUser.last_name = i['last_name']
            newUser.email = i['email']
            newUser.date_created=date.today()
            newUser.last_login=date.today()
            users.append(newUser)

    db.session.add_all(users)
    db.session.commit()

    subscriptions = [
        Subscription(
            start_date=date.today(),
            end_date=date.today(),
            status=True,
            user=users[0],
            plan=plans[0],
        ),
    ]

    db.session.add_all(subscriptions)
    db.session.commit()

    payments = [
        Payment(
            amount=39.99,
            payment_date=date.today(),
            payment_type="mastercard",
            subscription=subscriptions[0],
        ),
        Payment(
            amount=39.99,
            payment_date=date.today(),
            payment_type="mastercard",
            subscription=subscriptions[0],
        ),
        Payment(
            amount=39.99,
            payment_date=date.today(),
            payment_type="mastercard",
            subscription=subscriptions[0],
        ),
    ]

    db.session.add_all(payments)
    db.session.commit()

    tickets = [
        Ticket(
            issue_description="random issue description",
            date_created=date.today(),
            status="in progress",
            user=users[0],
        ),
        Ticket(
            issue_description="random issue description 2",
            date_created=date.today(),
            status="in progress",
            user=users[0],
        ),
        Ticket(
            issue_description="random issue description 3",
            date_created=date.today(),
            status="in progress",
            user=users[0],
        ),
        Ticket(
            issue_description="random issue description 4",
            date_created=date.today(),
            status="in progress",
            user=users[0],
        ),
        Ticket(
            issue_description="random issue description 5",
            date_created=date.today(),
            status="in progress",
            user=users[0],
        ),
        Ticket(
            issue_description="random issue description 6",
            date_created=date.today(),
            status="in progress",
            user=users[0],
        ),
    ]

    db.session.add_all(tickets)
    db.session.commit()

    products = [
        Product(
            product_name="software product #1",
            description="description of product #1",
            license="generate a JWT token later",
        ),
    ]

    db.session.add_all(products)
    db.session.commit()

    plan_products = [
        PlanProduct(
            plan=plans[0],
            product=products[0]
        ),
    ]

    db.session.add_all(plan_products)
    db.session.commit()