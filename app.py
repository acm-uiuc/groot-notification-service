# -*- coding: utf-8 -*-
'''
Copyright © 2017, ACM@UIUC
This file is part of the Groot Project.
The Groot Project is open source software, released under the University of
Illinois/NCSA Open Source License.  You should have received a copy of
this license in a file with the distribution.
'''

from flask import Flask, request
from settings import MYSQL, TWITTER as TWITTER_CREDENTIALS
from utils import send_error, send_success, send_validation_errors
from notification_clients import TwitterClient, SlackClient, EmailClient
from models import Notification
import os

import logging
logger = logging.getLogger('groot_credits_service')
logging.basicConfig(level="INFO")

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    MYSQL['user'],
    MYSQL['password'],
    MYSQL['host'],
    MYSQL['dbname']
)
app.config['JSONIFY_MIMETYPE'] = 'application/json; charset=UTF-8'

PORT = 1122
DEBUG = os.environ.get('NOTIFICATION_DEBUG', False)

SERVICE_CLIENTS = {
    'slack': SlackClient(),
    'email': EmailClient(),
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
        try:
            SERVICE_CLIENTS[service['name']].send(
                message=notification['message']
            )
        except Exception as e:
            logger.error(
                'Exception while sending notificaiton to {}: {}'.format(
                    service['name'], e
                )
            )
            return send_error('Error sending notification.', 500)

    return send_success('Notification(s) sent')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
