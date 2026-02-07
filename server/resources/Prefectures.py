from resources.BaseResource import BaseResource
from models.LocationModels.PrefectureModel import PrefectureModel

class PrefectureList(BaseResource):
    model = PrefectureModel

    field_map = {
        "prefectureName": "name",
        "prefectureJapaneseName": "japanese_name",
        "prefectureJapaneseSpelling": "japanese_spelling",
        "prefectureImg": "img",
        "prefectureCardImg": "card_img",
        "prefectureBannerImg": "banner_img",
        "prefectureInfo": "info",
        "prefecturePopulation": "population",
        "prefectureFlag": "flag"
    }

    def get(self):
        return self.get_all()
    
    def post(self):
        return self.post_instance()
    
class SpecificPrefecture(BaseResource):
    model = PrefectureModel

    field_map = {
        "prefectureName": "name",
        "prefectureJapaneseName": "japanese_name",
        "prefectureJapaneseSpelling": "japanese_spelling",
        "prefectureImg": "img",
        "prefectureCardImg": "card_img",
        "prefectureBannerImg": "banner_img",
        "prefectureInfo": "info",
        "prefecturePopulation": "population",
        "prefectureFlag": "flag"
    }

    def get(self, id):
        return self.get_specific(id)
    
    def patch(self, id):
        return self.patch_instance(id)
    
    def delete(self, id):
        return self.delete_instance(id)