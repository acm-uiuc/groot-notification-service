# -*- coding: utf-8 -*-
'''
Copyright © 2017, ACM@UIUC
This file is part of the Groot Project.
The Groot Project is open source software, released under the University of
Illinois/NCSA Open Source License.  You should have received a copy of
this license in a file with the distribution.
'''

from flask import Flask, request
from settings import (
    TWITTER as TWITTER_CREDENTIALS,
    SLACK_API_TOKEN,
    EMAIL as EMAIL_CREDENTIALS
)
import inspect
from utils import send_error, send_success, send_validation_errors
from notification_clients import (
    TwitterClient,
    SlackClient,
    EmailClient
)
from models import Notification
import os

import logging
logger = logging.getLogger('groot_notification_service')
logging.basicConfig(level="INFO")

app = Flask(__name__)
app.config['JSONIFY_MIMETYPE'] = 'application/json; charset=UTF-8'

PORT = 1122
DEBUG = os.environ.get('NOTIFICATION_DEBUG', False)

SERVICE_CLIENTS = {
    'slack': SlackClient(SLACK_API_TOKEN),
    'email': EmailClient(**EMAIL_CREDENTIALS),
    'twitter': TwitterClient(**TWITTER_CREDENTIALS)
}


@app.route('/notification', methods=['POST'])
def post_notification():
    data = request.get_json(force=True)

    if not data:
        return send_error('Could not parse JSON from request body')

    notification, errors = Notification().load(data)

    if errors:
        return send_validation_errors(errors)

    if not notification['services']:
        return send_error('Must specify services to send to')

    for service in notification['services']:
        if service['name'] not in SERVICE_CLIENTS:
            return send_error('Invalid service: {}'.format(service['name']))

        send_func = SERVICE_CLIENTS[service['name']].send
        for key in service.keys():
            if key != 'name' and key not in inspect.getargspec(send_func)[0]:
                return send_error('Invalid key for service "{}": {}'.format(
                    service['name'], key)
                )

        try:
            logger.info(
                'Sending notification through {}'.format(service['name'])
            )
            send_func(
                message=notification['message'],
                **{k: v for k, v in service.items() if k != 'name'}
            )
        except Exception as e:
            logger.error(
                'Exception while sending notification to {}: {}'.format(
                    service['name'], e
                )
            )
            return send_error(
                'Error sending notification to {}: {}'.format(
                    service['name'], e
                ),
                500
            )

    return send_success('Notification(s) sent')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
