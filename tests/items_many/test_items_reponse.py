import unittest
from run import app
from config.db import db


class TestItemsResponse(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.db = db.get_db()

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)

    def test_get_items_if_there_is_parameter_deleted_is_not_equal_true(self):
        response = self.client.get('/v2/items?delete=errei_no_trampo')
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json)
        self.assertEqual(response.json["error"], "Parameter deleted is not equal true.")

    def test_get_items_if_there_is_parameter_deleted(self):
        pass
