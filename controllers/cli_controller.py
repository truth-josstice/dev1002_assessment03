from flask import Blueprint
from init import db

from models.company import Company
from models.gyms import Gym
from models.users import User
from models.climbs import Climb
from models.attempts import Attempt

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
    db.session.commit()

    gyms = [
        Gym(
            city = "Melbourne",
            company_id = company1.id,
            street_address = "123 Fake Street",
            name = "The Gym"
        ),
        Gym(
            city = "Melbourne",
            company_id = company1.id,
            street_address = "456 New Fake Street",
            name = "The Gym 2"
        )
    ]
    db.session.add_all(gyms)

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

    db.session.add_all(users)
    db.session.commit()

    climbs = [
        Climb(
            user_id = users[0].id,
            gym_id = gyms[0].id,
            style="Slab",
            difficulty_grade = "Purple",
            set_date = "01/01/2025"
        ), 
        Climb(
            user_id = users[0].id,
            gym_id = gyms[0].id,
            style = "Dyno",
            difficulty_grade = "Blue",
            set_date = "01/01/2025"
        ), 
        Climb(
            user_id = users[1].id,
            gym_id = gyms[1].id,
            style = "Slab",
            difficulty_grade = "4",
            set_date = "03/01/2025"
        ), 
        Climb(
            user_id = users[1].id,
            gym_id = gyms[1].id,
            style = "Overhang",
            difficulty_grade = "6",
            set_date = "03/01/2025"
        )
    ]

    db.session.add_all(climbs)
    db.session.commit()

    attempts = [
        Attempt(
            user_id = users[0].id,
            climb_id = climbs[0].id,
            fun_rating = "4",
            comments = "This was hard, almost have it",
            attempt_date = "02/01/2025"
        ), 
        Attempt(
            user_id = users[0].id,
            climb_id = climbs[0].id,
            fun_rating = "4",
            comments = "This was fun! Got it on my second visit",
            completed = True,
            attempt_date = "04/01/2025"
        ), 
        Attempt(
            user_id = users[1].id,
            climb_id = climbs[2].id,
            fun_rating = "4",
            comments = "Almost there! just need to try again",
            attempt_date = "05/01/2025"
        ), 
        Attempt(
            user_id = users[1].id,
            climb_id = climbs[2].id,
            fun_rating = "5",
            comments = "Sent it weeeheew",
            completed = True,
            attempt_date = "05/01/2025"
        ),
        Attempt(
            user_id = users[1].id,
            climb_id = climbs[3].id,
            fun_rating = "5",
            comments = "Flashed it!",
            completed = True,
            attempt_date = "05/01/2025"
        )
    ]
    
    db.session.add_all(attempts)
    db.session.commit()

    print("Tables seeded...")