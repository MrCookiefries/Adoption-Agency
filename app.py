"""routes & views for adoption agency site"""

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet
from forms import EditPetForm, PetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption_agency"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "AGkajgea9i3kjaj45KDjskg"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)


connect_db(app)

@app.route("/")
def home_page():
    """shows the home page listing pets"""

    pets = Pet.query.all()

    return render_template(
        "pets.html",
        pets=pets
    )

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """shows the form to add a pet & creates it"""

    form = PetForm()
        
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        pet = Pet(**data)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    
    return render_template(
        "add-pet.html",
        form=form,
        submit="Submit"
    )

@app.route("/pets/<int:id>")
def show_pet(id):
    """shows the pet details for given pet"""

    pet = Pet.query.get_or_404(id)

    return render_template(
        "pet.html",
        pet=pet
    )

@app.route("/pets/<int:id>/edit", methods=["GET", "POST"])
def edit_pet(id):
    """shows edit pet form & saves changes"""

    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data
        pet.photo_url = url
        pet.notes = notes
        pet.available = available
        db.session.add(pet)
        db.session.commit()

        return redirect(f"/pets/{id}")
        
    return render_template(
        "edit-pet.html",
        form=form,
        submit="Save"
    )
    


