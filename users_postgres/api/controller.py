from flask import jsonify, request, abort
from flask_restful import Resource
import requests
from api.schema import users_schema, user_schema
from api.models import Users
from manage import db
from api.session import session


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
        with session() as db:
            db.add(user)
        # db.session.add(user)
        # db.session.commit()
        return jsonify({'status': 'ok'})


class UsersPut(Resource):
    def put(self, username):
        #auth = requests.get('auth/<{}>'.format(username))   # проверка авторизован польз. или нет
        # if auth.status_code == 500:
        #if auth['status'] == 'failed':
         #   return abort(500, 'User is not authorized')

        user = Users.query.filter_by(username=username).first_or_404()
        data = request.get_json() or {}
        #result = user_schema.load(data)
        #print('zzzzzzzz', result)
        from_model_atribure(data, user)
        # db.session.commit()
        session()
        return jsonify({'status': 'update_ok'})  # user_schema.jsonify(user)


def from_model_atribure(data, user, result=None, new_user=False):
    if result is not None and result.errors != {}:
        return abort(500, 'Incorrect data')
    for field in ['username', 'email', 'user_address']:
        if field in data:
            setattr(user, field, data[field])
        elif 'username' not in data and\
                'email' not in data and\
                'user_address' not in data:
            return abort(500, 'Incorrect data')
    if new_user and 'password_hash' in data:
        user.set_password(data['password_hash'])

# пароль не изменяется пока
