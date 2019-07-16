import unittest
from core.app import app
from tests.data_for_test import data_all_users, data_user
import json
from core.config import db



# тестовая бд
TEST_DB = 'postgresql://postgres:11111111@localhost:5432/test_users'

class FlaskTestApi(unittest.TestCase):
    def setUp(self):
        # self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB
        self.app = app.test_client()
        #db.init_app(self.app)
        with app.app_context():
            #db.drop_all()
            db.create_all()

        self.assertEqual(app.debug, False)

    def tearDown(self):
        db.session.remove()
        #db.drop_all()

    def test_post_user(self):
        post_data1 = {
            "create_user_date": "2019-07-11T10:03:18.674207+00:00",
            "email": "alice@example.com",
            "id": "ff766fb5-3c14-4b5c-852f-edbf3c69edd5",
            "password": "pbkdf2:sha256:150000$zyVFKuDh$c6be8077860dd825e72938d54cd372591fe449a5702842137fc8df057c820c3b",
            "user_address": "Pushkina,27",
            "username": "alice"
        }
        user1 = self.app.post('/users/api/users', data=json.dumps(post_data1), content_type='application/json')
        self.assertEqual(user1.status_code, 200)
        self.assertEqual(user1.content_type, 'application/json')

        post_data2 = {
            "create_user_date": "2019-07-11T10:03:18.674207+00:00",
            "email": "petya@example.com",
            "id": "10a30b55-ce6c-4187-9ac9-4bc9e06cd077",
            "password": "pbkdf2:sha256:150000$omDDQqu5$760ba3e19c541e573a54714eb45a905184b858a77f6be03d56ac8df0a67ff540",
            "user_address": "Kurchatova,2",
            "username": "petya"
        }
        user2 = self.app.post('/users/api/users', data=json.dumps(post_data2), content_type='application/json')
        self.assertEqual(user2.status_code, 200)
        self.assertEqual(user2.content_type, 'application/json')

        post_data3 = {
            "create_user_date": "2019-07-11T10:03:18.674207+00:00",
            "email": "kolya@gmail.com",
            "id": "d4a36dd3-6a50-47af-adaa-82fb5064be36",
            "password": "pbkdf2:sha256:150000$fpQAxYPN$09468fb8f2ac2e73055480fa04a568101a8dffa5c41bb45ad5728f1862177807",
            "user_address": "kirova,4",
            "username": "kolya"
        }
        user3 = self.app.post('/users/api/users', data=json.dumps(post_data3), content_type='application/json')
        self.assertEqual(user3.status_code, 200)
        self.assertEqual(user3.content_type, 'application/json')

    def test_get_all_users(self):
        users = self.app.get('/users/api/users')
        self.assertEqual(users.status_code, 200)

        content = json.loads(users.get_data(as_text=True))
        self.assertEqual(content, data_all_users)

    def test_get_user_without_password(self):
        user = self.app.get('/users/api/alice')
        self.assertEqual(user.status_code, 404)

        content = json.loads(user.get_data(as_text=True))
        self.assertEqual(content, {'Error': "'password'"})

    def test_get_none_user_404(self):
        user = self.app.get('/users/api/don')
        self.assertEqual(user.status_code, 404)

    '''
    def test_post_user(self):
        post_data = {
            'username': 'nina',
            'password_hash': 'nina',
            'email': 'nina@example.com',
            'user_address': 'Ninskaya,27'
        }
        user = self.app.post('/users/api/users', data=json.dumps(post_data), content_type='application/json')
        self.assertEqual(user.status_code, 200)
        self.assertEqual(user.content_type, 'application/json')
    '''

    def test_post_none_user(self):
        user = self.app.post('/users/api/users/', data=None)
        self.assertEqual(user.status_code, 404)

    def test_api_wrong_address(self):
        user = self.app.get('/users/download')
        self.assertEqual(user.status_code, 404)


if __name__ == "__main__":
    unittest.main()
