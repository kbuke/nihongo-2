from resources.BaseResource import BaseResource
from models.LocationModels.CityModel import CityModel

class CityList(BaseResource):
    model = CityModel

    field_map = {
        "cityName": "name",
        "japaneseCitySpelling": "japanese_spelling",
        "japaneseCityName": "japanese_name",
        "cityImg": "img",
        "cityCardImg": "card_img",
        "cityBannerImg": "banner_img",
        "cityInfo": "info",
        "cityPopulation": "population",
        "prefectureId": "prefecture_id",
        "prefectureCapital": "prefecture_capital"
    }

    def get(self):
        return self.get_all()
    
    def post(self):
        return self.post_instance()
    

class SpecificCity(BaseResource):
    model = CityModel

    field_map = {
        "cityName": "name",
        "japaneseCitySpelling": "japanese_spelling",
        "japaneseCityName": "japanese_name",
        "cityImg": "img",
        "cityCardImg": "card_img",
        "cityBannerImg": "banner_img",
        "cityInfo": "info",
        "cityPopulation": "population",
        "prefectureId": "prefecture_id",
        "prefectureCapital": "prefecture_capital"
    }

    def get(self, id):
        return self.get_specific(id)
    
    def patch(self, id):
        return self.patch_instance(id)
    
    def delete(self, id):
        return self.delete_instance(id)