from .controller import UsersPutGet, UsersPostGet
from .api import usr_api, bp
from .config import create_app

app = create_app()
app.register_blueprint(bp, url_prefix='/users')

usr_api.add_resource(UsersPostGet, '/api/users')
usr_api.add_resource(UsersPutGet, '/api/<username>')

# http GET http://localhost:5000/users/api/alice
# http GET http://localhost:5000/users/api/users
# http POST http://localhost:5000/users/api/users username=alice password_hash=dog email=alice@example.com user_address=Pushkina,27
# http PUT http://localhost:5000/users/api/alice email=kolya@example.com
