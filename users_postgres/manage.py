from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from core.config import Config


'''
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand

from core.app import app
# from core.config import db

manager = Manager(app)

manager.add_command('db', MigrateCommand)
'''

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# from core.api import bp as api_bp
# app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)


'''
from flask_script import Shell
from flask_migrate import MigrateCommand, Manager
from core.config import db, migrate
from core.app import app
from core.models import Users


manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, Users=Users)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    #app.run(debug=True)
'''