from flask import Blueprint
from init import db

from models.company import Company
from models.gyms import Gym
from models.users import User

db_commands = Blueprint("db", __name__)

@db_commands .cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created...")

@db_commands .cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped...")

@db_commands .cli.command("seed")
def seed_tables():
    company1 = Company(
        name = "Company 1",
        website = "www.website.com"
    )
    db.session.add(company1)

    gym1 = Gym(
        city = "Melbourne",
        street_address = "123 Fake Street",
        name = "The Gym"
    )
    db.session.add(gym1)

    users = [
        User(
            username = "username1",
            password="securepassword123",
            email="email@email.com",
            first_name="First",
            last_name="Last",
            climbing_ability="Beginner"
        ), 
        User(
            username = "username2",
            password="securepassword1234",
            email="email1@email.com",
            first_name="First",
            last_name="Last",
            climbing_ability="Intermediate"
        )
    ]

    db.session.commit()
    print("Tables seeded...")