from flask import Blueprint
from flask_restful import Api
from flask_jwt_extended import JWTManager

api_bp = Blueprint('api', __name__)  # Creating a Blueprint object for our API routes
api = Api(api_bp)  # Creating an Api object for our API
jwt = JWTManager(api_bp)  # Creating a JWTManager object for handling JWTs

# Import API routes here

from . import authentication, data_processing, exportData, importData, schedule, user  # Importing the API routes from each module
