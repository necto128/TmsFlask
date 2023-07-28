from marshmallow import Schema, fields


class IdeaSchema(Schema):
    type = fields.Str(validate=fields.Length(max=100), required=True)
    activity = fields.Str(validate=fields.Length(max=100), required=True)
    accessibility = fields.Float(required=True)
    price = fields.Float(required=True)
    user_id = fields.Int()

    class Meta:
        unknown = 'exclude'


class UserSchema(Schema):
    username = fields.Str(required=True, validate=fields.Length(min=6, max=16))
    password = fields.Str(required=True, validate=fields.Length(min=8, max=16))
    idea = fields.Int(required=False)
