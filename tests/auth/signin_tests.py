import unittest
from ctypes import cdll

from app.app import create_app, db
from flask import url_for
from mod_auth.models import User
from mod_memory.models import Memory
from mod_memory.memory_types import MemoryTypes
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

    
    def add_user_to_test_db(self):
        user_to_add = 'walter@example.com'
        response = self.client.post(url_for('auth.signup'), data=dict(
            user_name=user_to_add,
            password='qwqwqwqwqw'
        ), follow_redirects=True)

        return response

    def test_signup_user(self):
        print("Running Test: ", self._testMethodName)
        user_to_add = 'walter@example.com'
        response = self.add_user_to_test_db()

        self.assertEqual(response.status_code, 200)
        user = User.query.filter_by(email=user_to_add).first()
        self.assertEqual(user.is_authenticated(), False)

    def test_user_login(self):
        print("Running Test: ", self._testMethodName)

        user_to_add = 'walter@example.com'
        response = self.client.post(url_for('auth.signup'), data=dict(
            user_name=user_to_add,
            password='qwqwqwqwqw'
        ), follow_redirects=True)

        print("Signed up user")

    def test_query_memories(self):
        print("Running Test: ", self._testMethodName)

        resp = self.add_user_to_test_db()
        self.assertEqual(resp.status_code, 200)

        user_to_add = 'walter@example.com'
        user = User.query.filter_by(email=user_to_add).first()

        # Add memories for this user.
        mem_name = "Tumultuous"
        mem_info = "making a loud, confused noise; uproarious."
        new_mem = Memory(mem_name, mem_info, MemoryTypes.VOCABULARY)
        user.memories.append(new_mem)

        db.session.commit()

        response = self.client.post(url_for('app.get_memories'), data=dict(
            memories_needed=3
        ), follow_redirects=True)
        
        print(response.data)