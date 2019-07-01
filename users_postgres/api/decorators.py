'''
from manage import db
from flask import request

def dec(func):
    def decorator(*args, **kwargs):
        data = request.get_json() or {}
        try:
            if 'username' in data and 'email' in data and 'password_hash' in data:
                db.session.commit()
            db.session.rollback()
            raise
        except('Bad')
'''

