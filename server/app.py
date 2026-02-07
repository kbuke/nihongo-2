from config import app, api

from resources.Prefectures import PrefectureList, SpecificPrefecture
from resources.Cities import CityList, SpecificCity
from resources.Users import UsersList, SpecificUser
from resources.VerifyUser import VerifyUser

api.add_resource(PrefectureList, "/prefectures")
api.add_resource(SpecificPrefecture, "/prefectures/<int:id>")

api.add_resource(CityList, "/cities")
api.add_resource(SpecificCity, "/cities/<int:id>")

api.add_resource(UsersList, "/users")
api.add_resource(SpecificUser, "/users/<int:id>")

api.add_resource(VerifyUser, "/users/verify")


if __name__ == "__main__":
    app.run(port = 5555, debug = True)