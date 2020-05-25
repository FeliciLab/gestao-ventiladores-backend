from application import app
from unittest import TestCase
from config.db import db


class BaseCase(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db


    def tearDown(self):
        pass
