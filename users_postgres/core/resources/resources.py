from flask import request
from flask_restful import Resource

from core.models import Users
from core.utils.schema import user_schema, user_schema_put, user_schema_patch, user_schema_auth
from core.controllers.controllers import answer_resource_methods
from core.controllers.controllers import UsersController


class UsersResourceCreate(Resource):
    def get(self):
        all_users = UsersController().get_all()
        return user_schema.dump(all_users, many=True).data, 200

    def post(self):
        data = request.get_json() or {}
        result, errors = user_schema.load(data)
        user_check_post = UsersController().post_user(result, errors)
        usr = Users.query.filter(Users.username == user_check_post).first()
        return answer_resource_methods(user_schema.dump(usr).data), 201


class UsersResourceChange(Resource):
    def put(self, id):
        data = request.get_json() or {}
        result, errors = user_schema_put.load(data)
        user_check_put = UsersController().put_user(id, result, errors)
        return answer_resource_methods(user_schema.dump(user_check_put).data), 200

    def patch(self, id):
        data = request.get_json() or {}
        result, errors = user_schema_patch.load(data)
        user_check_patch = UsersController().patch_user(id, result, errors)
        return answer_resource_methods(user_schema.dump(user_check_patch).data), 200

    def get(self, id):
        user = UsersController().get_user(id)
        return answer_resource_methods(user_schema.dump(user).data), 200


class UsersResourceAuth(Resource):
    def post(self):
        data = request.get_json() or {}
        result, errors = user_schema_auth.load(data)
        user_check_authoriz = UsersController().post_auth(result, errors)
        return answer_resource_methods(user_schema.dump(user_check_authoriz).data), 200
