import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from core.config import Config

engine = sqlalchemy.create_engine(Config.SQLALCHEMY_DATABASE_URI)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def connect_session_db(func):
    def inner(*args, **kwargs):
        session = Session()
        try:
            data = func(*args, **kwargs)
            session.commit()
        except Exception as err:
            session.rollback()
            raise err
        finally:
            Session.remove()
        return data
    return inner
