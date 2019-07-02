from flask import Blueprint
from flask_restful import Api
# from .controller import UsersPostGet, UsersPutGet

bp = Blueprint('users', __name__)
api = Api(bp)

# usr_api.add_resource(UsersGetAll, 'users')
# usr_api.add_resource(UsersGet, '/users/<username>')
