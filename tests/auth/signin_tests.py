import unittest
from ctypes import cdll

from app.app import create_app, db
from flask import url_for
from mod_auth.models import User

"""
Authentication Tests

Run command:
python -m unittest tests\auth\signin_tests.py
"""
class AuthenticationTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup Class method ")

    @classmethod
    def tearDownClass(cls):
        print("TearDown Class method")

    def setUp(self):
        self.app = create_app('testing')
        # To allow assertions and errorrs to be propagated up.
        self.app.testing = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        print("Creating test tables")
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)
        self._ctx = self.app.test_request_context()
        self._ctx.push()

    def tearDown(self):
        print("Dropping all test tables")
        db.session.commit()
        db.drop_all()


    def test_signup_user(self):
        print("Running Test: ", self._testMethodName)
        user_to_add = 'jason@example.com'
        response = self.client.post(url_for('auth.signup'), data=dict(
            user_name=user_to_add,
            password='qwqwqwqwqw'
        ), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        print("testyyyy 11111111111")
        user = User.query.filter_by(email=user_to_add).first()
        print("testyyyy 22222222222")
        self.assertEqual(user.is_authenticated(), False)

