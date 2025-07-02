from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.auth import api as auth_ns
from flask_bcrypt import Bcrypt
def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    bcrypt = Bcrypt()
    app.config.from_object(config_class)
    app.config['JWT_SECRET_KEY'] = 'c999f61d1e154e16fa1f0336af0d15e12cc810f5797cb6dd6997571950802f94'
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    jwt = JWTManager()
    jwt.init_app(app)
    bcrypt.init_app(app)
    # Register the users namespace
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(auth_ns, path='/api/v1/auth')
    return app