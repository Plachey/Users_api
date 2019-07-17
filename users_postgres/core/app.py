from core.api import usr_api, bp
#from core.config import create_app, psgres_url
from core.resources.resources import UsersResourceCreate, UsersResourceChange

#app = create_app()
#app.register_blueprint(bp, url_prefix='/users')

from flask import Flask
from core.config import runtime_config, db, migrate, Config
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(bp, url_prefix='/users')

usr_api.add_resource(UsersResourceCreate, '/api/users')
usr_api.add_resource(UsersResourceChange, '/api/<id>')


'''
from flask import g
from sqlalchemy.orm import sessionmaker
@app.before_request
def open_session():
    g.conn = psgres_url()
    session = sessionmaker()
    session.configure(bind=g.conn)
    g.session = session()


@app.after_request
def close_session(e):
    if e is None:
        g.session.commit()
    else:
        g.session.rollback()

    g.session.close()
    g.session = None
'''
