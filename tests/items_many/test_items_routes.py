import unittest
from run import app
from config.db import db
from time import sleep

class TestItemsRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.db = db.get_db()

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)

    def test_items_has_get_route(self):
        response = self.client.get('/v2/items')
        self.assertEqual(response.status_code, 200)

    def test_get_items_if_there_is_parameter_deleted_is_not_equal_true(self):
        response = self.client.get('/v2/pass?deleted=errei_no_trampo')
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json)
        self.assertEqual(response.json["error"], "Parameter deleted is not equal true.")

    def test_get_items_if_there_is_parameter_deleted(self):
        response_right = self.client.get('/v2/items?deleted=true')
        self.assertEqual(response_right.status_code, 200)
        self.assertIn('deleted', response_right.json)
        self.assertEqual(response_right.json['deleted'], True)
    
    def test_get_items_if_there_is_not_parameter_deleted(self):
        response_right = self.client.get('/v2/items')
        self.assertEqual(response_right.status_code, 200)
        self.assertIn('deleted', response_right.json)
        self.assertEqual(response_right.json['deleted'],False)
