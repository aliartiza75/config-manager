###################################################################################################
# Summary: This file contains routes for configuration manager service
###################################################################################################
import os
import sys
import json
from flask import Blueprint
from flask import request, jsonify, abort
mod = Blueprint('config_manager', __name__)


@mod.route('/config_manager/healthcheck', methods=['GET'])
def health_check():
    '''
    It will be used to verify the status of api
    '''
    response = {}
    response['message'] = 'Api is in healthy state'
    return jsonify(response)

