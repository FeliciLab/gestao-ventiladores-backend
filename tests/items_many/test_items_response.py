from ..base_case import BaseCase
from bson import ObjectId

class TestItemsResponse(BaseCase):
    # GET testes
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

    def test_get_items_has_field_content(self):
        response = self.client.get('v2/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn('content', response.json)

    # POST testes
    def test_post_items_has_json(self):
        response = self.client.post('/v2/items', data={'content': [self.mock_items['valido']]})
        self.assertEqual(type(response.json), dict)
    
    def test_post_items_has_field_content_list(self):
        response = self.client.post('/v2/items', data={'content': [self.mock_items['valido']]})
        self.assertIn('content', response.json)
        self.assertEqual(type(response.json['content']), list)

    def test_post_items_has_valid_id(self):
        response = self.client.post('/v2/items', data={'content': [self.mock_items['valido']]})
        for _id in response.json['content']:
            str_id = ObjectId(_id)
            self.assertEqual(type(str_id), str)

