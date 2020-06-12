from tests.base_case import BaseCase
from bson import ObjectId
import copy
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
            self.assertNotEqual(type(document['_id']), dict)

    def test_get_items_has_no_mongo_date(self):
        response = self.client.get('v2/items')

        for document in response.json['content']:
            self.assertNotEqual(type(document['created_at']), dict)
            self.assertNotEqual(type(document['updated_at']), dict)
            if 'deleted_at' in document:
                self.assertNotEqual(type(document['deleted_at']), dict)

    def test_get_items_has_field_content(self):
        response = self.client.get('v2/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn('content', response.json)

    # POST testes
    def test_post_items_has_json(self):
        response = self.many_make_post(self.mock_items['valido'])
        self.assertEqual(type(response.json), dict)

    def test_post_items_has_field_content_list(self):
        response = self.many_make_post(self.mock_items['valido'])
        self.assertIn('content', response.json)
        self.assertEqual(type(response.json['content']), list)

    def test_items_valid_body(self):
        response = self.many_make_post(self.mock_items['valido'])
        self.assertEqual(response.status_code, 201)

    def test_items_has_id_in_body(self):
        payload = copy.deepcopy(self.mock_items['valido'])
        payload['_id'] = '5edf7f75bc2462d2bcc12d8b5'
        response = self.many_make_post(payload)
        self.assertIn('ID must not be sent', response.json['error'][0]['0'])

    # PATCH
    def test_patch_items_has_empty_body(self):
        
        response = self.many_make_post(self.mock_items['valido'])

        payload = self.get_mock('item', 'valido_patch')
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

        for key, value in response.json['error'][0].items():
            if isinstance(value, list):
                for message in value:
                    self.assertEqual('Unknown field.', message)

    def test_patch_items_has_invalid_id(self):
        payload = self.mock_items['valido_patch']

        _id = 'aa202020'
        payload['_id'] = _id
        payload = json.dumps({'content': [payload]})

        response = self.client.patch(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid ID', response.json['error'][0]['0'])

    def test_patch_items_has_nonexistent_id(self):
        payload = self.mock_items['valido_patch']

        _id = '5ecc5e521ef64069c005338a'
        payload['_id'] = _id
        payload = json.dumps({'content': [payload]})

        response = self.client.patch(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('Nonexistent ID', response.json['error'][0]['0'])

    # DELETE
    def test_delete_items_has_empty_body(self):
        response = self.many_make_post(self.mock_items['valido'])
        payload = json.dumps({'content': [response.json['content'][0]]})
        response = self.client.delete(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)

        self.assertEqual(response.json, '')
        self.assertEqual(response.status_code, 200)

    def test_delete_accept_only_string_list(self):
        payload = json.dumps({'sample': 'wrong'})
        response = self.client.delete(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)
        for item in response.json:
            self.assertEqual(type(item), str)

    def test_delete_items_has_invalid_id(self):
        _id = 'aa202020'
        payload = json.dumps({'content': [_id]})

        response = self.client.delete(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid ID', response.json['error'][0]['0'])

    def test_patch_items_has_nonexistent_id(self):

        _id = '5ecc5e521ef64069c005338a'
        payload= json.dumps({'content': [_id]})

        response = self.client.delete(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('Nonexistent ID', response.json['error'][0]['0'])

