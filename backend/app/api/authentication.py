from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from ..models.user import User
from ..extensions import bcrypt

class SignupAPI(Resource):
    def post(self):
        # Signup logic here
        pass

class LoginAPI(Resource):
    def post(self):
        # Login logic here
        pass

api.add_resource(SignupAPI, '/signup')  # Adding the SignupAPI resource to our API at the /signup route
api.add_resource(LoginAPI, '/login')  # Adding the LoginAPI resource to our API at the /login route
