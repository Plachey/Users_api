from werkzeug.security import generate_password_hash, check_password_hash
from core.models import Users
from core.config import db
from flask import abort
from core.controllers.session import Session, connect_session_db


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

    def __init__(self, data, errors):
        self._data = data
        self._errors = errors

    @connect_session_db
    def post_user(self):
        session = Session()
        if self._errors:
            abort(404, f'Invalid data: {self._errors}')
        username = self._data["username"]
        email = self._data["email"]
        user_address = self._data["user_address"]
        password = set_password(self._data["password"], Users)
        user = Users(username=username, email=email, password=password, user_address=user_address)
        session.add(user)
        #db.session.add(user)
        #db.session.commit()
        return username

    @connect_session_db
    def put_user(self, id):
        session = Session()
        user = Users.query.filter(Users.id == id).first()
        if not user:
            abort(404, 'No user with that id')
        if self._errors:
            abort(404, f'Invalid data{self._errors}')
        session.query(Users).filter(Users.id == id).update({
            "username": self._data["username"],
            "email": self._data["email"],
            "user_address": self._data["user_address"],
            "password": set_password(self._data["password"], user)
        })
        #db.session.commit()
        return user

    @connect_session_db
    def patch_user(self, id):
        session = Session()
        user = Users.query.filter(Users.id == id).first()
        if not user:
            abort(404, 'No user with that name')
        if self._errors:
            abort(404, f'Invalid data{self._errors}')

        # if 'username' in self._data:
        #     user.username = self._data['username']
        # if 'password' in self._data:
        #     user.password = set_password(self._data["password"], user)
        # if 'email' in self._data:
        #     user.email = self._data['email']
        # if 'user_address' in self._data:
        #     user.user_address = self._data['user_address']

        for field in ['username', 'email', 'user_address']:
            if field in self._data:
                session.query(Users).filter(Users.id == id).update({f"{field}": self._data[field]})
            if 'password' in self._data:
                session.query(Users).filter(Users.id == id).update({
                    "password": set_password(self._data["password"], user)})

        #db.session.commit()
        return user

    '''
    def post_auth(self, id):
        user = db.session.query(Users).filter_by(id=id).first()
        if not user:
            abort(404, 'No user with that id')
        if self._errors:
            abort(404, f'Invalid data{self._errors}')
        username = self._data['username']
        password = check_password(user.password, self._data['password'])
        if username != user.username or password is False:
            abort(404, 'Incorrect username or password')
        return user
    '''
