# -*- coding: utf-8 -*-
'''
Copyright © 2017, ACM@UIUC
This file is part of the Groot Project.
The Groot Project is open source software, released under the University of
Illinois/NCSA Open Source License.  You should have received a copy of
this license in a file with the distribution.
'''

from flask import make_response, jsonify
import logging
logger = logging.getLogger('groot_notification_service.utils')


def send_error(message, code=400):
    return make_response(jsonify(dict(error=message)), code)


def send_success(message, code=200):
    return make_response(jsonify(dict(message=message)), code)


def send_validation_errors(errors, code=400):
    return make_response(jsonify(dict(errors=errors)), code)
