# -*- coding: utf-8 -*-
'''
Copyright © 2017, ACM@UIUC
This file is part of the Groot Project.
The Groot Project is open source software, released under the University of
Illinois/NCSA Open Source License.  You should have received a copy of
this license in a file with the distribution.
'''

from marshmallow import Schema, fields


class Service(Schema):
    name = fields.Str(required=True)
    recipients = fields.List(fields.Str())
    sender = fields.Str()
    subject = fields.Str()


class Notification(Schema):
    services = fields.Nested(Service, many=True, required=True)
    message = fields.Str(required=True)
