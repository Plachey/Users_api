from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

from .api import bp, api

def create_app():
    app = Flask(__name__)
    api.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'postgresql://postgres:11111111@localhost:5432/users'
    app.register_blueprint(bp)
    with app.app_context():
        db.init_app(app)
    #migrate.init_app(app=app, db=db)
    return app