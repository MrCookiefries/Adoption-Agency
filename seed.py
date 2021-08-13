"""seeds the database"""

from random import randint, sample

from app import app
from models import db, Pet

db.drop_all()
db.create_all()

# Pets - 10
names = [
    "Snudge", "Borker", "Carter", "Mr. Hops", "Hedge",
    "Woofer", "Whiskers", "Jumbo", "Socks", "Little Paw"
]
all_species = {
    "cat", "dog", "porcupine"
}
pets = []

for name in names:
    species = sample(all_species, 1)[0]
    age = randint(1, 8)
    available = False if age <= 2 else True
    pet = Pet(name=name, species=species, age=age, available=available)
    pets.append(pet)

db.session.add_all(pets)
db.session.commit()
