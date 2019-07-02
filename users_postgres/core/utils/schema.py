from marshmallow import Schema, fields
# from marshmallow import ValidationError


class UsersSchema(Schema):
    id = fields.UUID()
    username = fields.Str()
    email = fields.Email()
    password_hash = fields.Str()
    user_address = fields.Str()
    create_user_date = fields.DateTime()

    class Meta:
        fields = ('id', 'username', 'email', 'password_hash', 'user_address', 'create_user_date')


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
