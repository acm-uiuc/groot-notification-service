# -*- coding: utf-8 -*-
'''
Copyright © 2017, ACM@UIUC
This file is part of the Groot Project.
The Groot Project is open source software, released under the University of
Illinois/NCSA Open Source License.  You should have received a copy of
this license in a file with the distribution.
'''

from smtplib import SMTP

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from exceptions import ClientException


class EmailClient:
    def __init__(self, host=None, port=None, username=None, password=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def send(self,
             message,
             recipients=None,
             sender=None,
             subject=None,
             mimetype='plain'):
        if not sender.endswith('@acm.illinois.edu'):
            raise ClientException(
                'Invalid email. Must be an acm.illinois.edu email'
            )

        conn = SMTP(host=self.host, port=self.port)
        conn.starttls()

        if self.username and self.password:
            conn.login(self.username, self.password)

        email_message = MIMEMultipart()
        email_message['From'] = sender
        email_message['Subject'] = subject
        email_message.attach(MIMEText(message, mimetype))

        for recipient in recipients:
            email_message['To'] = recipient
            conn.sendmail(sender, recipient, email_message.as_string())

        conn.quit()
