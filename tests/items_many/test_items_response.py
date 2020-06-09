from ipdb import set_trace
from tests.base_case import BaseCase
from bson import ObjectId
import json

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
        payload = json.dumps({'content': [self.mock_items['valido']]})
        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)
        self.assertEqual(type(response.json), dict)
    
    def test_post_items_has_field_content_list(self):
        payload = json.dumps({'content': [self.mock_items['valido']]})
        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)
        self.assertIn('content', response.json)
        self.assertEqual(type(response.json['content']), list)

    # PUT
    def test_put_items_has_empty_body(self):
        payload_post = json.dumps({'content' : [self.mock_items['valido']]})

        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload_post)

        payload = self.mock_items['valido_patch']
        id = response.json['content'][0]
        payload['_id'] = id
        payload = json.dumps({'content': [payload]})
        
        response = self.client.put(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)
        self.assertEqual(response.json, '')
        self.assertEqual(response.status_code, 200)

    def test_put_items_not_valid_body(self):
        pass
    
    def test_put_items_has_not_content_in_body(self):
        pass

    def test_put_items_has_invalid_list_dict_items(self):
        pass

    def test_put_items_has_valid_id(self):
        pass

    # PATCH
    def test_patch_items_has_empty_body(self):
        payload_post = json.dumps({'content' : [self.mock_items['valido']]})

        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload_post)

        payload = self.mock_items['valido_patch']
        id = response.json['content'][0]
        payload['_id'] = id
        payload = json.dumps({'content': [payload]})
        
        response = self.client.patch(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)
        self.assertEqual(response.json, '')
        self.assertEqual(response.status_code, 200)
        

    def test_patch_items_has_wrong_field(self):
        payload = self.mock_items['invalido_patch']
        payload = json.dumps({'content': [payload]})

        response = self.client.patch(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)

        for key, value in response.json['error']['0'].items():
            if isinstance(value, list):
                for message in value:
                    self.assertEqual('Unknown field.', message)

    def test_patch_items_has_invalid_id(self):
        payload = self.mock_items['valido_patch']

        id = 'aa202020'
        payload['_id'] = id
        payload = json.dumps({'content': [payload]})

        response = self.client.patch(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid ID', response.json['error'][0]['0'])

    def test_patch_items_has_nonexistent_id(self):
        payload = self.mock_items['valido_patch']

        id = '5ecc5e521ef64069c005338a'
        payload['_id'] = id
        payload = json.dumps({'content': [payload]})

        response = self.client.patch(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('Nonexistent ID', response.json['error'][0]['0'])
