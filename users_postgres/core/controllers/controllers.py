from werkzeug.security import generate_password_hash, check_password_hash
from core.models import Users
from core.config import db


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

    def create_user(self):

        username = self._data["username"],
        email = self._data["email"],
        user_address = self._data["user_address"],
        password = set_password(self._data["password"], Users)
        user = Users(username=username, email=email, password=password, user_address=user_address)
        db.session.add(user)
        db.session.commit()
        return user.id
