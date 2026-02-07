from resources.BaseResource import BaseResource
from models.UserModels.UserModel import UserModel
from datetime import datetime 

from config import db
     
class UsersList(BaseResource):
    model = UserModel

    field_map = {
        "userName": "name",
        "userEmail": "email",
        "userPic": "profile_picture",
        "userInfo": "info",
        "userPassword": "password_hash"
    }

    def after_create(self, user):
        # Force unverified state
        user.is_verified = False
        user.verified_at = None
        db.session.commit()

        # Send verification email
        user.send_verification_email()
    
    def get(self):
        return self.get_all()
    
    def post(self):
        return self.post_instance()

class SpecificUser(BaseResource):
    model = UserModel

    field_map = {
        "userName": "name",
        "userEmail": "email",
        "userPic": "profile_picture",
        "userInfo": "info",
        "userPassword": "password_hash"
    }

    def get(self, id):
        return self.get_specific(id)
    
    def delete(self, id):
        return self.delete_instance(id)
    
    def patch(self, id):
        return self.patch_instance(id)

