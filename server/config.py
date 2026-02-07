from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy import MetaData
from flask_mail import Mail
from dotenv import load_dotenv
# Create passkey for project and then download load_dotenv from dotenv below
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = os.getenv("APP_SECRET_KEY")

app.config["MAIL_USERNAME"] = os.getenv("EMAIL_ADDRESS")
app.config["MAIL_PASSWORD"] = os.getenv("GMAIL_APP_PW")
app.config["FRONTEND_URL"] = os.getenv("FRONTEND_URL")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("EMAIL_ADDRESS")
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False

mail = Mail(app)


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
})
db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

bcrypt = Bcrypt(app)

api = Api(app)

CORS(app, supports_credentials=True)


