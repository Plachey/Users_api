from flask import jsonify, request, abort
from flask_restful import Resource
import requests
from api.schema import users_schema, user_schema
from api.models import Users
from manage import db


class UsersGetAll(Resource):
    def get(self):
        all_users = Users.query.all()
        result = users_schema.dump(all_users)
        return jsonify(result.data)


class UsersGet(Resource):
    def get(self, username):
        user = Users.query.filter_by(username=username).first_or_404()
        result = user_schema.dump(user)
        return jsonify(result.data)


class UsersPost(Resource):
    def post(self):
        data = request.get_json() or {}
        user = Users()
        result = user_schema.load(data)
        from_model_atribure(data, user, result, new_user=True)
        db.session.add(user)
        db.session.commit()
        return jsonify({'status': 'ok'})


class UsersPut(Resource):
    def put(self, username):
        auth = requests.get('auth/<{}>'.format(username))   # проверка авторизован польз. или нет
        # if auth.status_code == 500:
        if auth['status'] == 'failed':
            return abort(500, 'User is not authorized')

        user = Users.query.filter_by(username=username).first_or_404()
        data = request.get_json() or {}
        result = user_schema.load(data)
        from_model_atribure(data, user, result)
        db.session.commit()
        return jsonify({'status': 'ok'})  # user_schema.jsonify(user)


def from_model_atribure(data, user, result, new_user=False):
    if result.errors != {}:
        return abort(500, 'Incorrect data')
    for field in ['username', 'email', 'user_address']:
        if field in data:
            setattr(user, field, data[field])
    if new_user and 'password_hash' in data:
        user.set_password(data['password_hash'])
