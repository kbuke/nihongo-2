from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from flask import current_app
from flask_mail import Message
from config import mail
from flask import current_app

from config import db, bcrypt

import re

from Validations.validate_uniqueness import validate_uniqueness

class UserBase(db.Model, SerializerMixin):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False) # ensure it is a legitimate email address
    profile_picture = db.Column(db.String, nullable = True) # set a default image if none is entered
    info = db.Column(db.String, nullable = True) # limit amount of words
    _password_hash = db.Column(db.String, nullable = False)

    # ----------------------------- Send Confirmation Email -----------------------------
    is_verified = db.Column(db.Boolean, nullable = False, default = False)
    verified_at = db.Column(db.DateTime, nullable = True)

    # Generate secure verification token
    @staticmethod
    def generate_verification_token(email):
        serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        return serializer.dumps(email, salt="email-verification")
    
    # Verify the token
    @staticmethod
    def verify_verification_token(token, max_age=3_600):
        serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        try:
            email = serializer.loads(
                token,
                salt="email-verification",
                max_age=max_age
            )
        except(BadSignature, SignatureExpired):
            return None 
        return email
    
    # Send email - but use platform like MailGun in actual deployment
    def send_verification_email(self):
        token = self.generate_verification_token(self.email)

        verify_url = (
            f"{current_app.config['FRONTEND_URL']}"
            f"/verify?token={token}"
        )

        msg = Message(
            subject="Confirm your email",
            recipients=[self.email],
            body=f"""
                Hi!

                Please confirm your email by clicking the link below:

                {verify_url}

                This link expires in 1 hour.
            """
        )

        print(f"Sending email to {self.email} with URL: {verify_url}")
        mail.send(msg)


    # ----------------------------- Validate Email -----------------------------
    @validates("email")
    def validate_email(self, key, value):
        email_pattern = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
        if not re.match(email_pattern, value):
            raise ValueError("Please enter a valid email address")
        
        return value

    # ----------------------------- Hash Password -----------------------------
    @hybrid_property
    def password_hash(self):
        raise AttributeError("password: write-only attribute")

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)
    
    def __init__(self, **kwargs):
        password = kwargs.pop("password_hash", None)
        super().__init__(**kwargs)

        if password:
            self.password_hash = password

