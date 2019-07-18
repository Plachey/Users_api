from core.api import usr_api, bp
from core.resources.resources import UsersResourceCreate, UsersResourceChange


from flask import Flask
from core.config import runtime_config, db, migrate
app = Flask(__name__)
app.config.from_object(runtime_config())
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(bp, url_prefix='/users')

usr_api.add_resource(UsersResourceCreate, '/api/users')
usr_api.add_resource(UsersResourceChange, '/api/<id>')
