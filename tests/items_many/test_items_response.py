from ..base_case import BaseCase


class TestItemsResponse(BaseCase):
    """def setUp(self):
        self.client = app.test_client()
        self.db = db.get_db()

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)"""

    def test_get_items_has_field_content_list(self):
        response = self.client.get('/v2/items')
        self.assertIn('content', response.json)
        self.assertEqual(type(response.json['content']), list)

    def test_get_items_has_json(self):
        response = self.client.get('/v2/items')
        self.assertEqual(type(response.json), dict)

    def test_get_items_has_id(self):
        response = self.client.get('/v2/items')
        response.json['content'].append({'_id': 'value'})
        for document in response.json['content']:
            self.assertNotEqual(document.get('_id'), None)

    def test_get_items_has_no_mongo_oid(self):
        response = self.client.get('/v2/items')
        for document in response.json['content']:
            self.assertIn(document['_id'], '$oid')

    def test_get_items_has_no_mongo_date(self):
        response = self.client.get('v2/items')
        for document in response.json['content']:
            self.assertNotIn('$date', document['created_at'])
            self.assertNotIn('$date', document['updaed_at'])
            if 'delted_at' in document:
                self.assertNotIn('$date', document['deleted_at'])

    def test_get_items_success_has_field_content(self):
        response = self.client.get('v2/items')
        self.assertEqual(response.status_code, 200)
        for document in response.json:
            self.assertIn('content', document)

    def test_get_items_error_has_field_error(self):
        response = self.client.get('v2/items')
        self.assertEqual(response.status_code, 400)
        for document in response.json:
            self.assertIn('error', document)
