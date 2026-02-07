from flask import request
from flask_restful import Resource
from models.UserModels.UserModel import UserModel
from config import db
from datetime import datetime

class VerifyUser(Resource):
    def post(self):
        data = request.get_json()
        token = data.get("token")
        if not token:
            return {"error": "Missing token"}, 400

        email = UserModel.verify_verification_token(token)
        if not email:
            return {"error": "Invalid or expired token"}, 400

        # Find user by email
        user = UserModel.query.filter_by(email=email).first()
        if not user:
            return {"error": "User not found"}, 404

        # Mark as verified
        user.is_verified = True
        user.verified_at = datetime.utcnow()
        db.session.commit()

        return {"message": "Email verified successfully!"}, 200
