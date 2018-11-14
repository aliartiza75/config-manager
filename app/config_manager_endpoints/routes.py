###################################################################################################
# Summary: This file contains routes for configuration manager service
###################################################################################################
import os
import sys
import json
from flask import Blueprint
from mongoengine import *
from flask import request, jsonify, abort
mod = Blueprint('config_manager', __name__)


mongo_db_name = os.environ['MONGO_DB_NAME']
mongo_ip = os.environ['MONGO_DB_IP']
mongo_port = int(os.environ['MONGO_DB_PORT'])

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

from services import config_service as conf_service

@mod.route('/v1/config/healthcheck', methods=['GET'])
def health_check():
    '''
    It will be used to verify the status of api
    '''
    response = {}
    response['message'] = 'Api is in healthy state'
    return jsonify(response)


@mod.route('/v1/config/', methods=['GET'])
def get_config():
    '''
    It will be used to verify the status of api
    '''
    response = {}
    response['message'] = 'Api is in healthy state'
    
    connect(mongo_db_name, host=mongo_ip, port=mongo_port)
    
    try:
        cf_obj = conf_service.ConfigurationManager(tenant="a", integration_type="b", configuration={})
        cf_obj.save()
    except Exception as e:
        response['message'] = str(e)
    return jsonify(response)

@mod.route('/v1/config/', methods=['POST'])
def create_config():
    '''
    It will be used to verify the status of api
    '''
    response = {}
    response['message'] = 'Api is in healthy state'
    connect(mongo_db_name, host=mongo_ip, port=mongo_port)
    try:
        cf_obj = conf_service.ConfigurationManager(tenant="a", integration_type="b", configuration={})
        s = conf_service.ConfigurationManager.objects(tenant="a", integration_type="b")
        # print(dir(s))
        print(s.to_json())
    except Exception as e:
        response['message'] = str(e)
    return jsonify(response)

    return jsonify(response)