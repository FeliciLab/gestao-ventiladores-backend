import unittest
from run import app
from config.db import db

class TestItemsRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.db = db.get_db()

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)

    def test_items_has_get_route(self):
        response = self.client.get('/v2/items')
        self.assertEquals(response.status_code, 200)

    def test_items_has_post_route(self):
        response = self.client.post('/v2/items')
        self.assertEquals(response.status_code, 200)

    def test_items_has_put_route(self):
        pass

    def test_items_has_patch_route(self):
        pass

    def test_items_has_delete_route(self):
        pass
