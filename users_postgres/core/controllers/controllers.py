from flask import abort
from werkzeug.security import generate_password_hash, check_password_hash

from core.controllers.session import Session, connect_session_db
from core.models import Users


def set_password(password, user):
    user.hash_password = generate_password_hash(password)
    return user.hash_password


def check_password(hash_password, password):
    return check_password_hash(hash_password, password)


def answer_resource_methods(data):
    return {
            "id": data["id"],
            "username": data["username"],
            "email": data["email"],
            "user_address": data["user_address"],
            "create_user_date": data["create_user_date"]
        }


class UsersController:
    def get_all(self):
        all_users = Users.query.all()
        if not all_users:
            abort(404, 'No users')
        return all_users

    @connect_session_db
    def post_user(self, data, errors):
        session = Session()
        if errors:
            abort(404, f'Invalid data: {errors}')
        username = data["username"]
        email = data["email"]
        user_address = data["user_address"]
        password = set_password(data["password"], Users)
        user = Users(username=username, email=email, password=password, user_address=user_address)
        session.add(user)
        return username

    @connect_session_db
    def put_user(self, id, data, errors):
        session = Session()
        user = Users.query.filter(Users.id == id).first()
        if not user:
            abort(404, 'No user with that id')
        if errors:
            abort(404, f'Invalid data{errors}')
        session.query(Users).filter(Users.id == id).update({
            "username": data["username"],
            "email": data["email"],
            "user_address": data["user_address"],
            "password": set_password(data["password"], user)
        })
        return user

    @connect_session_db
    def patch_user(self, id, data, errors):
        session = Session()
        user = Users.query.filter(Users.id == id).first()
        if not user:
            abort(404, 'No user with that name')
        if errors:
            abort(404, f'Invalid data{errors}')

        for field in ['username', 'email', 'user_address']:
            if field in data:
                session.query(Users).filter(Users.id == id).update({f"{field}": data[field]})
            if 'password' in data:
                session.query(Users).filter(Users.id == id).update({
                    "password": set_password(data["password"], user)})
        return user

    def get_user(self, id):
        user = Users.query.filter(Users.id == id).first()
        if not user:
            abort(404, 'No user with that id')
        return user

    '''
    def post_auth(self, id, data, errors):
        user = db.session.query(Users).filter_by(id=id).first()
        if not user:
            abort(404, 'No user with that id')
        if self._errors:
            abort(404, f'Invalid data{errors}')
        username = data['username']
        password = check_password(user.password, data['password'])
        if username != user.username or password is False:
            abort(404, 'Incorrect username or password')
        return user
    '''
