from flask import make_response, jsonify
import logging
logger = logging.getLogger('groot_credits_service.utils')


def send_error(message, code=400):
    return make_response(jsonify(dict(error=message)), code)


def send_success(message, code=200):
    return make_response(jsonify(dict(message=message)), code)


def send_validation_errors(errors, code=400):
    return make_response(jsonify(dict(errors=errors)), code)
