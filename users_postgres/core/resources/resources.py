from flask import request, abort
from flask_restful import Resource

from core.models import Users
from core.utils.schema import user_schema, user_schema_put, user_schema_auth, user_schema_patch
#from core.utils.session import session
from core.config import db
from core.controllers.controllers import answer_resource_methods
from core.controllers.controllers import UsersController


class UsersResourceCreate(Resource):
    def get(self):
        all_users = db.session.query(Users).all()
        return user_schema.dump(all_users, many=True).data

    def post(self):
        data = request.get_json() or {}
        result, errors = user_schema.load(data)
        user_check_post = UsersController(data, errors).post_user()
        print(user_check_post)
        usr = Users.query.filter(Users.username == user_check_post).first()
        return answer_resource_methods(user_schema.dump(usr).data), 201


class UsersResourceChange(Resource):
    '''
    def post(self, id):
        data = request.get_json() or {}
        result, errors = user_schema_authorization.load(data)
        user_check_authoriz = UsersController(data, errors).post_auth(id)
        return answer_resource_methods(user_schema.dump(user_check_authoriz).data), 200
    '''
    def put(self, id):
        data = request.get_json() or {}
        result, errors = user_schema_put.load(data)
        user_check_put = UsersController(result, errors).put_user(id)
        return answer_resource_methods(user_schema.dump(user_check_put).data), 200

    def patch(self, id):
        data = request.get_json() or {}
        result, errors = user_schema_patch.load(data)
        user_check_patch = UsersController(result, errors).patch_user(id)
        return answer_resource_methods(user_schema.dump(user_check_patch).data), 200

    def get(self, id):
        user = db.session.query(Users).filter_by(id=id).first()
        if not user:
            abort(404, 'No user with that id')
        #data = request.get_json() or {}
        #if not user:
         #   abort(404, 'No user with that name')
        #elif data['password'] is None or check_password(user.password, data['password']) is False:
         #   abort(404, 'Password none or incorrect')
        #res = user_schema.dump(user).data
        return answer_resource_methods(user_schema.dump(user).data), 200
