###################################################################################################
# Summary: This file contains routes for configuration manager service
###################################################################################################
# sys modules
import os
import sys
import json
from flask import Blueprint
from mongoengine import *
from flask import request, jsonify, abort
mod = Blueprint('config_manager', __name__)


# Dev defined modules
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
from services import config_manager_service as config_manager_ser
from services import response_service as resp_service


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
    response = {'data': {}}
    valid_query_params = False
    # extracting query params
    if ("tenant" in request.args) and ("integration_type" in request.args):
        tenant = request.args['tenant']
        integration_type = request.args['integration_type']
        valid_query_params = True

    if valid_query_params:
        # creating configuration mananger class object
        conf_manager_serv_obj = config_manager_ser.ConfigurationManagerService()

        # check database connection status
        if conf_manager_serv_obj.connection_status:

            records_extraction, result = conf_manager_serv_obj.get_record(tenant, integration_type)
            # check for record extraction
            if records_extraction:
                response['data'].update({'message': "Document has been retrieved"})
                result['_id'] = str(result['_id'])
                response['data'].update({'data': result})
                response['data'].update({'status': resp_service.status['OK']})
            else:
                response['data'].update({'message': result})
                response['data'].update({'status': resp_service.status['UNPROCESSABLE']})
        else:
            response['data'].update({'connection_status': ks_obj.check_conn_status()})
            response['data'].update({'status': resp_service.status['INTERNAL_SERVER_ERROR']})
    else:
        response['data'].update({'message': 'Invalid query data'})
        response['data'].update({'status': resp_service.status['BAD_REQUEST']})
    return jsonify(response)


@mod.route('/v1/config/', methods=['POST'])
def create_config():
    '''
    It will be used to verify the status of api
    '''
    response = {'data': {}}
    req_body_keys = list(request.json)
    valid_query_params = False
    if ('tenant' in req_body_keys) and ('integration_type' in req_body_keys) and ('configuration' in req_body_keys):
        tenant = request.json['tenant']
        integration_type = request.json['integration_type']
        configuration = request.json['configuration']
        valid_query_params = True

    if valid_query_params:
        # creating configuration mananger class object
        conf_manager_serv_obj = config_manager_ser.ConfigurationManagerService()

        # check database connection status
        if conf_manager_serv_obj.connection_status:

            record_inserted, result = conf_manager_serv_obj.insert_record(tenant, integration_type, configuration)
            # check for record extraction
            if record_inserted:
                response['data'].update({'message': "Document has been inserted"})
                response['data'].update({'status': resp_service.status['OK']})
            else:
                response['data'].update({'message': result})
                response['data'].update({'status': resp_service.status['UNPROCESSABLE']})
        else:
            response['data'].update({'connection_status': ks_obj.check_conn_status()})
            response['data'].update({'status': resp_service.status['INTERNAL_SERVER_ERROR']})

    else:
        response['data'].update({'message': 'Invalid query data'})
        response['data'].update({'status': resp_service.status['BAD_REQUEST']})

    return jsonify(response)
