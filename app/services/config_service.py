###################################################################################################
# Summary: File contains code for configuration manager service
###################################################################################################
import os
import sys
from pymongo import MongoClient
from mongoengine import *
import datetime


class ConfigurationManager(Document):
    
    tenant = StringField(required=True, max_length=100)
    integration_type = StringField(required=True, max_length=100)
    configuration = DictField()
    created_at = DateTimeField(default=datetime.datetime.now)
