from ..application import app
from unittest import TestCase
from mongoengine import connect


class BaseCase(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = connect('db_test_scripts')


    def tearDown(self):
        pass
