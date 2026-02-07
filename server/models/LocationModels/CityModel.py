from sqlalchemy.orm import validates
from sqlalchemy import text

from models.LocationModels.LocationBase import LocationBase

from config import db

from HelperFunctions.BelongsTo import belongs_to
from HelperFunctions.ExcludeInfo import exclude_info

from Validations.validate_id_int import validate_id_int
from Validations.validate_instance_exists import validate_instance_exists

from models.LocationModels.PrefectureModel import PrefectureModel

class CityModel(LocationBase):
    __tablename__ = "cities"

    prefecture_capital = db.Column(db.Boolean, nullable = False, server_default=text("false"))

    prefecture_id = belongs_to("prefectures")

    serialize_rules = (
        *exclude_info(
            "prefecture",
            "info",
            "population",
            "japanese_name",
            "flag",
            "cities",
            "img",
            "banner_img"
        ),
    )

    @validates("prefecture_id")
    def validate_prefecture(self, key, value):
        value = validate_id_int(value, key)

        value = validate_instance_exists(PrefectureModel, value, key)

        return value
