from marshmallow import Schema, fields


class Service(Schema):
    name = fields.Str(required=True)
    recipients = fields.List(fields.Str())
    sender = fields.Str()
    subject = fields.Str()


class Notification(Schema):
    services = fields.Nested(Service, many=True, required=True)
    message = fields.Str(required=True)
