from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .extensions import bcrypt  # Importing the bcrypt extension from our custom extensions file

app = Flask(__name__)
CORS(app)  # Setting up CORS to allow cross-origin requests
app.config.from_object('config.Config')  # Loading the app configuration from a Config object
db = SQLAlchemy(app)  # Creating a SQLAlchemy database object
ma = Marshmallow(app)  # Creating a Marshmallow object for object serialization and deserialization
jwt = JWTManager(app)  # Creating a JWTManager object for handling JWTs

from .api import api_bp
app.register_blueprint(api_bp, url_prefix='/api')  # Registering the api_bp Blueprint with the app

bcrypt.init_app(app)  # Initializing the bcrypt extension with our Flask app
