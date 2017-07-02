import unittest, sys
from ctypes import cdll

from app.app import create_app, db
from flask import url_for
from mod_auth.models import User
from mod_memory.models import Memory
from mod_memory.memory_types import MemoryTypes


"""
Memory Tests

Run command:
python -m unittest tests\auth\memory_tests.py
"""
class MemoryTests(unittest.TestCase):

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

    
    def test_create_memory(self):
        print("Running Test: ", self._testMethodName)

    def test_edit_memory(self):
        print("Running Test: ", self._testMethodName)