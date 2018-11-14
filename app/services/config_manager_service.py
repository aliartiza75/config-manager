###################################################################################################
# Summary: File contains code for configuration manager Model
###################################################################################################
import os
import sys
import json
from pymongo import MongoClient
from mongoengine import *
import datetime


mongo_db_name = os.environ['MONGO_DB_NAME']
mongo_ip = os.environ['MONGO_DB_IP']
mongo_port = int(os.environ['MONGO_DB_PORT'])


# Importing models
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))


class ConfigurationManagerService():

    def __init__(self):
        '''
        Class constructor
        '''
        self.connection_status = False

        try:
            client = MongoClient(mongo_ip, mongo_port)
            self.db = client[mongo_db_name]
            self.connection_status = True
        except Exception as e:
            self.connection_status = False

    def insert_record(self, tenant, integration_type, configuration):
        '''
        It will insert a document in database
        '''
        try:
            config_manager_collection_obj = self.db.configuration_manager
            # check if record exists
            record_exists = config_manager_collection_obj.find_one({"tenant": tenant, "integration_type": integration_type})
            if (record_exists):
                del record_exists['_id']
                new_record = {"$set": {"tenant": tenant,
                                       "integration_type": integration_type,
                                       "configuration": configuration
                                       }
                              }
                # updating
                config_manager_collection_obj.update_one(record_exists, new_record)
            # record doesn't already exist
            else:
                cm_document = {
                    "tenant": tenant,
                    "integration_type": integration_type,
                    "configuration": configuration
                }
                config_manager_collection_obj.insert_one(cm_document)

            return True, 'Record has been inserted'
        except Exception as e:
            return False, str(e)

    def get_record(self, tenant, integration_type):
        '''
        It will extract a document based on its tenant and configurations
        '''
        try:
            config_manager_collection_obj = self.db.configuration_manager
            record_exists = config_manager_collection_obj.find_one({"tenant": tenant, "integration_type": integration_type})
            if record_exists:
                return True, record_exists
            else:
                return False, "No record exists"

        except Exception as e:
            return False, "Unable to extract information %s" % (e)
