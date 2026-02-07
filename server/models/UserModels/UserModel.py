from sqlalchemy.orm import validates

from config import db

from models.UserModels.UserBase import UserBase

from Validations.validate_uniqueness import validate_uniqueness

class UserModel(UserBase):
    __tablename__ = "users"

    email = db.Column(db.String, nullable = False, unique = True)

    @validates("email")
    def validate_email(self, key, value):
        value = super().validate_email(key, value)
        
        return validate_uniqueness(value, self, UserModel, key, "Email Address")


    # Set up relations with:
        # City: Wishlist, Visited
