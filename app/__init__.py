import os
from app.config_manager_endpoints.routes import mod
from flask import Flask, Blueprint
from flask_api import FlaskAPI
app = Flask(__name__)

# add mongo url to flask config, so that flask_pymongo can use it to make connection
app.config['MONGO_URI'] = os.environ.get('MONGO_DB_URI')
mongo = PyMongo(app)
from app.config_manager import *

# registering application
app.register_blueprint(mod, uri_prefix='/config_manager')
