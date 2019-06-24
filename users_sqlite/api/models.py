from api.manage import db, ma, bcrypt
import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    address = db.Column(db.Text(200))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return '<User {}'.format(self.username)

    def set_password(self, password_hash):
        self.password_hash = bcrypt.generate_password_hash(password_hash)

    def check_password(self, password_hash):
        return bcrypt.check_password_hash(self.password_hash, password_hash)


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'password_hash', 'address', 'date')


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
