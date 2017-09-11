# -*- coding: utf-8 -*-
'''
Copyright © 2017, ACM@UIUC
This file is part of the Groot Project.
The Groot Project is open source software, released under the University of
Illinois/NCSA Open Source License.  You should have received a copy of
this license in a file with the distribution.
'''

from slackclient import SlackClient as SlackAPIClient


class SlackClient:
    def __init__(self, slack_token):
        self.client = SlackAPIClient(slack_token)

    def send(self, message, recipients=None):
        for recipient in recipients:
            self.client.api_call(
                'chat.postMessage',
                channel=recipient,
                text=message
            )
