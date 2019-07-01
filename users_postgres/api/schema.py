from marshmallow import Schema, fields
from marshmallow import ValidationError


def valid_email(email):
    if email is None or email is '':
        raise ValidationError("Incorrect email")


def valid_password_hash(password_hash):
    if password_hash is None or password_hash is '':
        raise ValidationError("Incorrect password_hash")


def valid_username(username):
    if username is None or username is '':
        raise ValidationError("Incorrect username")


class UsersSchema(Schema):
    # id = fields.UUID()
    username = fields.Str(required=True, validate=valid_username)
    email = fields.Email(required=True, validate=valid_email)
    password_hash = fields.Str(required=True, validate=valid_password_hash)
    user_address = fields.Str()
    # create_user_date = fields.DateTime()

    class Meta:
        fields = ('id', 'username', 'email', 'password_hash', 'user_address', 'create_user_date')


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
