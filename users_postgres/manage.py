from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from api.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/')

if __name__ == '__main__':
    app.run()
