from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from core.api import usr_api

db = SQLAlchemy()
migrate = Migrate()



import os
import logging
class Config:
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '11111111')
    DEFAULT_DB = os.environ.get('DEFAULT_DB', 'users')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DEBUG = False
    HOST = '127.0.0.1'
    LOG_LEVEL = logging.INFO
    TOKEN = os.environ.get('TOKEN', None)
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DEFAULT_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    LOG_LEVEL = logging.ERROR


class DevConfig(Config):
    DEBUG = True


def runtime_config():
    env = os.environ.get("APP_ENV", "dev").strip().lower()
    if env == "prod":
        return ProdConfig

    return DevConfig
'''
def psgres_url():
    return 'postgresql://postgres:11111111@localhost:5432/users'


def create_app():
    app = Flask(__name__)
    usr_api.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = psgres_url()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
    return app
'''