from datetime import date
from flask import Blueprint
from models.user import User
from models.subscription import Subscription
from models.payment import Payment
from models.support_ticket import Ticket
from models.plan import Plan
from models.product import Product
from models.subscription_details import SubscriptionDetail
from app import db, bcrypt
import json, random
from security.auth import generate_license

cli_commands = Blueprint('cli', __name__)

@cli_commands.cli.command("create")
def database_create():
    print("Droppping tables")
    db.drop_all()
    print("Dropped tables")
    print("Creating tables")
    db.create_all()
    print("Created tables")
    print("Seeding tables")
    #four types of plans
    plans = [
        Plan(
            plan_name="Free",
            description="Access to service is free, can use upto 2 products",
            price=0,
            length=1000,
            product_limit=2
        ),
        Plan(
            plan_name="Basic",
            description="Provides basic access to service, comes with use of 4 products",
            price=15.99,
            length=30,
            product_limit=4
        ),
        Plan(
            plan_name="Advanced",
            description="Provides advanced access to service, comes with use of 5 products",
            price=29.99,
            length=30,
            product_limit=5
        ),
        Plan(
            plan_name="Pro",
            description="Provides professional access to service, comes with use of 6 products",
            price=49.99,
            length=30,
            product_limit=6
        ),
    ]

    db.session.add_all(plans)
    db.session.commit()

    #seed all user details from dummy_users.json file
    users = []
    with open("seed_data/dummy_users.json") as f:
        data = json.load(f)
        for i in data:
            users.append(
                User(
            first_name = i['first_name'],
            last_name = i['last_name'],
            email = i['email'],
            #password = bcrypt.generate_password_hash(i["password"]).decode("utf8"),
            password = "hello",
            date_created=date.today(),
            last_login=date.today(),
            ))

    db.session.add_all(users)
    db.session.commit()

    #for each user in users[], generate a random subscription (random amount of plans, random active/disabled, assigned to user)
    subscriptions = []
    for index, val in enumerate(users):
        for j in range(random.randint(1, 4)):
            subscriptions.append(
            Subscription(
                start_date=date.today(),
                end_date=date.today(),
                status=random.choice([True, False]),
                user=users[index],
                plan=plans[random.randint(0, 3)],
            ))

    db.session.add_all(subscriptions)
    db.session.commit()

    #for each entry in subscriptions[], create a payment with the correct price depending that associated subscriptions plan
    payments = []   
    for index, val in enumerate(subscriptions):
        #print((plans[(subscriptions[index].plan_id) - 1]).price)
        for j in range(random.randint(1, 10)):
            payments.append(
                Payment(            
                    amount=(plans[(subscriptions[index].plan_id) - 1]).price,
                    payment_date=date.today(),
                    payment_type=random.choice(["mastercard", "visa", "amex", "paypal", "eft"]),
                    subscription=subscriptions[index],
                ))
    db.session.add_all(payments)  #wtf? db.session.add_all() causes session to fail?
    db.session.commit()

    #for each user in users[], generate a random amount of support tickets between 0 and 3
    tickets = []
    for index, val in enumerate(users):
        with open("seed_data/dummy_tickets.json") as f:
            data = json.load(f)          
            for j in range(random.randint(1, 4)):
                tickets.append(Ticket(
                    issue_description = random.choice(data)['description'],
                    date_created=date.today(),
                    status=random.choice(["in progress", "closed"]),
                    user=users[index],
                ))

    db.session.add_all(tickets)
    db.session.commit()

    #loads all products available from dummy_products.json and populates associated database entity
    products = []
    with open("seed_data/dummy_products.json") as f:
        data = json.load(f)
        for i in data:
            products.append(Product(
                product_name = i['product_name'],
                description = i['description'],
            ))

    db.session.add_all(products)
    db.session.commit()

    #associates each subscription with a plan and its associated products
    subscription_details = []
    for i in subscriptions:
        populate_products = i.plan.product_limit
        for j in range(populate_products):
            subscription_details.append(SubscriptionDetail(
                license = generate_license(),
                plan_id = i.plan.id,
                product_id = random.choice(products).id,
                subscription_id = i.id
            ))

    print("Seeded tables")
    db.session.add_all(subscription_details)
    db.session.commit()

#@cli_commands.cli.command("test")