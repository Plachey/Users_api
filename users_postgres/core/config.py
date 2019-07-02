import os
from flask import Flask
#from core.database import db
#from .api import api
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate


class Config(object):
    UPLOAD_FOLDER = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # url = 'postgresql://{}:{}@{}:{}/{}'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:11111111@localhost:5432/users'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


'''
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    api.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'postgresql://postgres:11111111@localhost:5432/users'
    # app.register_blueprint(bp)
    with app.app_context():
        db.init_app(app)
    migrate.init_app(app=app, db=db)
    return app
'''


'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .api import bp, api
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    api.init_app(app)
    UPLOAD_FOLDER = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # url = 'postgresql://{}:{}@{}:{}/{}'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:11111111@localhost:5432/users'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    bcrypt = Bcrypt(app)
    #app.config.from_object(Config)
    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
    return app
'''
