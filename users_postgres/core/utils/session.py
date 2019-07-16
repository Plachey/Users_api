from contextlib import contextmanager

import sqlalchemy
from sqlalchemy.orm import sessionmaker

#from core.config import psgres_url

#engine = sqlalchemy.create_engine(psgres_url())
#Session = sessionmaker(bind=engine)

'''
from flask import g
from functools import wraps
from sqlalchemy.orm import sessionmaker
from core.config import create_app

def establish_connection(x_client: str = None):
    def actual_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            g.conn = create_app()
            Session = sessionmaker()
            Session.configure(bind=g.conn)
            g.session = Session()
            return func(*args, **kwargs)

        return func_wrapper

    return actual_decorator


def kill_session(e):
    if e is None:
        g.session.commit()
    else:
        g.session.rollback()

    g.session.close()
    g.session = None



@contextmanager
def session(auto_commit=True):
    session = Session()
    try:
        yield session
        if auto_commit:
            session.commit()
    except Exception as err:
        session.rollback()
        raise err
    finally:
        session.close()

def dbconnect(func):
    def inner(*args, **kwargs):
        session = Session()  # with all the requirements
        try:
            func(*args, session=session, **kwargs)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
    return inner
'''
