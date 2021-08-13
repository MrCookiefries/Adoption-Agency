"""FSQLA models for the database"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """connects app to the database"""
    db.app = app
    db.init_app(app)

# https://www.freepik.com/free-icon/animal-paw-print_774725.htm
# Photo taken from source ^ on August 11th, 2021
default_pet_photo_url = "https://image.flaticon.com/icons/png/512/64/64431.png"

class Pet(db.Model):
    """model for pets"""

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(15),
        nullable=False
    )
    species = db.Column(
        db.String(20)
    )
    photo_url = db.Column(
        db.String,
        default=default_pet_photo_url
    )
    age = db.Column(
        db.Integer
    )
    notes = db.Column(
        db.String
    )
    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    def __repr__(self):
        id = self.id; n = self.name; s = self.species; ag = self.age; av = self.available
        return f"<Pet id={id} name={n} species={s} age={ag} available={av}>"

