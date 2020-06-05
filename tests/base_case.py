from unittest import TestCase
from run import app
from config.db import db
from .mocks.mock_items import mock_items


class BaseCase(TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.db = db.get_db()
        self.mock_items = mock_items

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
