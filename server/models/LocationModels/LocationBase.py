from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

from Validations.validate_string import validate_string
from Validations.validate_uniqueness import validate_uniqueness

from config import db

class LocationBase(db.Model, SerializerMixin):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    japanese_spelling = db.Column(db.String, nullable = False)
    japanese_name = db.Column(db.String, nullable = False)
    img = db.Column(db.String, nullable = False)
    card_img = db.Column(db.String, nullable = False)
    banner_img = db.Column(db.String, nullable = True)
    info = db.Column(db.String, nullable = False)
    population = db.Column(db.BigInteger, nullable = False)

    #-------------------------------------- Validate Name --------------------------------------
    @validates("name")
    def validate_location_name(self, key, value):
        return validate_string(value, "Location Name")
    
    #-------------------------------------- Validate Images --------------------------------------
    @validates("img", "card_img")
    def validate_location_images(self, key, value):
        return validate_string(value, "Location Images")
    
    #-------------------------------------- Convert Population Number to String --------------------------------------
    @property
    def population_display(self):
        value = self.population

        if value > 150_000_000:
            raise ValueError("Population of Japan is not greater than 150million")
        
        if value >= 1_000_000:
            return f"{round(value / 1_000_000)} Million"
        
        if value >= 1_000:
            return f"{round(value / 1_000)} Thousand"
        
        return str(value)
