"""forms for the site"""

from flask_wtf import FlaskForm
from wtforms.fields import TextField, SelectField, BooleanField
from wtforms.fields.html5 import URLField, IntegerField
from wtforms.validators import InputRequired, Length, Optional, NumberRange, URL

class PetForm(FlaskForm):
    """form for a pet"""

    name = TextField("Name of pet", validators=[
        InputRequired(message="Pet must have a name!"),
        Length(max=15, message="Name cannot be longer than %(max)d!")
    ])
    species = SelectField("Spcecies of pet", validators=[
        InputRequired(message="Pet must have a species!"),
        Length(max=20, message="Name cannot be longer than %(max)d!")
    ], choices=[
        ("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")
    ])
    photo_url = URLField("URL to photo of pet", validators=[
        Optional(),
        URL(message="Must be a valid image link!")
    ])
    age = IntegerField("Age of pet (in years)", validators=[
        Optional(),
        NumberRange(min=0, max=30, message="Pet age must be between %(min)d & %(max)d!")
    ])
    notes = TextField("Notes about the pet", validators=[
        Optional()
    ])

class EditPetForm(FlaskForm):
    """form to edit pet details"""

    photo_url = URLField("URL to photo of pet", validators=[
        Optional(),
        URL(message="Must be a valid image link!")
    ])
    notes = TextField("Notes about the pet", validators=[
        Optional()
    ])
    available = BooleanField("Available to adopt?", validators=[
        Optional()
    ])

