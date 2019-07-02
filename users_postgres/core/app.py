from .controller import UsersPostGet, UsersPutGet
from .api import bp, api
#from .config import create_app
from manage import app

#app = create_app()
app.register_blueprint(bp)

api.add_resource(UsersPutGet, '/users/<username>')
api.add_resource(UsersPostGet, '/users')

# http GET http://localhost:5000/users/alice
# http GET http://localhost:5000/users
# http POST http://localhost:5000/users username=alice password_hash=dog email=alice@example.com user_address=Pushkina,27
# http PUT http://localhost:5000/users/alice email=kolya@example.com