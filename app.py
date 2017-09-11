# -*- coding: utf-8 -*-
'''
Copyright © 2017, ACM@UIUC
This file is part of the Groot Project.
The Groot Project is open source software, released under the University of
Illinois/NCSA Open Source License.  You should have received a copy of
this license in a file with the distribution.
'''

from flask import Flask
from settings import MYSQL
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

PORT = 8765
DEBUG = os.environ.get('NOTIFICATION_DEBUG', False)


@app.route('/notification', methods=['POST'])
def post_notification():
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
