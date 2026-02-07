from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

from Validations.validate_uniqueness import validate_uniqueness
from Validations.validate_string import validate_string
from Validations.validate_instance_numbers import validate_instance_numbers

from config import db

from models.LocationModels.LocationBase import LocationBase

from Validations.validate_instance_exists import validate_instance_exists

from HelperFunctions.ExcludeInfo import exclude_info

class PrefectureModel(LocationBase):
    __tablename__ = "prefectures"

    name = db.Column(db.String, unique = True, nullable = False)
    flag = db.Column(db.String, unique = True, nullable = False)

    cities = db.relationship("CityModel", backref = "prefecture", lazy = True)

    serialize_rules = (
        *exclude_info(
            "cities",
            "prefecture", 
            "population",
            "banner_img",
            "img",
            "prefecture_id",
            "japanese_name",
            "info"
        ),
    )

    #-------------------------------------- Validate Prefecture Name --------------------------------------
    @validates("name")
    def validate_location_name(self, key, value):
        value = super().validate_location_name(key, value)

        value = validate_uniqueness(value, self, PrefectureModel, key, "Prefecture")

        # Japan has 47 prefectures
        value = validate_instance_numbers(PrefectureModel, self, 47, key, value)

        return value 
    
    #-------------------------------------- Validate Prefecture Flag --------------------------------------
    @validates("flag")
    def validate_prefecture_flag(self, key, value):
        value = validate_string(value, "Prefecture Flag")

        value = validate_uniqueness(value, self, PrefectureModel, key, "Prefecture Flag")

        return value

