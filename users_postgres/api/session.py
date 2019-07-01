from contextlib import contextmanager

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from config import Config

engine = sqlalchemy.create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)


@contextmanager
def session(auto_commit=True):
    session = Session()
    try:
        yield session
        if auto_commit:
            session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

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
