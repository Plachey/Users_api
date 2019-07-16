from flask import request, abort
from flask_restful import Resource

from core.models import Users
from core.utils.schema import user_schema, user_schema_put
#from core.utils.session import session
from core.config import db
from core.controllers.controllers import set_password, check_password, answer_resource_methods

from sqlalchemy.exc import SQLAlchemyError
from core.controllers.controllers import UsersController

class UsersResourceCreate(Resource):
    def get(self):
        all_users = db.session.query(Users).all()
        return user_schema.dump(all_users, many=True).data

    def post(self):
        data = request.get_json() or {}
        result, errors = user_schema.load(data)
        if errors:
            abort(404, 'Invalid data')
        '''
        #try:
            user = Users(username=data["username"],
                         email=data["email"],
                         user_address=data["user_address"],
                         password=set_password(data["password"], Users))
        
            #with session() as ses:
            db.session.add(user)
            db.session.commit()
        '''
        user_check_post = UsersController(data, errors).create_user()
        usr = db.session.query(Users).filter_by(id=user_check_post).first()
        res = user_schema.dump(usr).data
        return answer_resource_methods(res), 201
        #except Exception as er:
         #   db.session.rollback()
          #  return {"Error": str(er)}, 404


class UsersResourceChange(Resource):
    """
    def get(self, username):
        user = db.session.query(Users).filter_by(username=username).first()
        data = request.get_json() or {}
        #try:
        if not user:
            abort(404, 'No user with that name')
        elif data['password'] is None or check_password(user.password, data['password']) is False:
            abort(404, 'Password none or incorrect')

        res = user_schema.dump(user).data
        return answer_resource_methods(res), 200
        #except Exception as er:
            #return {"Error": str(er)}, 404
    """
    def post(self, id):
        user = db.session.query(Users).filter_by(id=id).first()
        data = request.get_json() or {}
        # try:
        if not user:
            abort(404, 'No user with that name')
        elif data['password'] is None or check_password(user.password, data['password']) is False:
            abort(404, 'Password none or incorrect')

        res = user_schema.dump(user).data
        return answer_resource_methods(res), 200

    def put(self, id):
        user = db.session.query(Users).filter_by(id=id).first()
        if not user:
            abort(404, 'No user with that name')

        data = request.get_json() or {}
        result, errors = user_schema_put.load(data)
        if errors:
            abort(404, 'Invalid data')
        #try:
        db.session.query(Users).filter_by(id=id).update({
                "username": data["username"],
                "email": data["email"],
                "user_address": data["user_address"],
                "password": set_password(data["password"], user)
        })
        db.session.commit()

        res = user_schema.dump(user).data
        return answer_resource_methods(res), 200
        #except Exception as er:
         #   db.session.rollback()
          #  return {"Error": str(er)}, 404

    '''
    def put(self, username):
        user = db.session.query(Users).filter_by(username=username).first()
        if not user:
            abort(404, 'No user with that name')

        data = request.get_json() or {}
        result, errors = user_schema_put.load(data)
        if errors:
            abort(404, 'Invalid data')

        with session() as ses:
            ses.query(Users).filter_by(username=username).update({
                "username": data["username"],
                "email": data["email"],
                "user_address": data["user_address"],
                "password": set_password(data["password"], user)
            })

        res = user_schema.dump(user).data
        return answer_resource_methods(res)
    '''

    def patch(self, id):
        user = db.session.query(Users).filter_by(id=id).first()
        if not user:
            abort(404, 'No user with that name')

        data = request.get_json() or {}
        result, errors = user_schema_put.load(data)
        #usern = data['username']
        if errors:
            abort(404, 'Invalid data')
        #with session() as ses:
        for field in ['username', 'email', 'user_address']:
            if field in data:
                db.session.query(Users).filter_by(id=id).update({f"{field}": data[field]})
            if 'password' in data:
                db.session.query(Users).filter_by(id=id).update({
                    "password": set_password(data["password"], user)})
        db.session.commit()

        #user = db.session.query(Users).filter_by(username=usern).first()
        res = user_schema.dump(user).data
        return answer_resource_methods(res), 200
