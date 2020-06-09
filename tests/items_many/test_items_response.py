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

    def test_items_valid_body(self):
        payload_post2 = json.dumps({'content': [self.mock_items['valido']]})
        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload_post2)
        self.assertEqual(response.status_code, 201)

    def test_items_has_id_in_body(self):
        payload = copy.deepcopy(self.mock_items['valido'])
        payload['_id'] = '5edf7f75bc2462d2bcc12d8b5'
        payload = json.dumps({'content': [payload]})
        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)
        self.assertIn('ID must not be sent', response.json['error'][0]['0'])

    # PUT
    def test_put_items_has_empty_body(self):
        payload_post = json.dumps({'content': [self.mock_items['valido']]})
        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload_post)

        payload = copy.deepcopy(self.mock_items['somente_obrigatorios'])
        id = response.json['content'][0]
        payload['_id'] = id
        payload = json.dumps({'content': [payload]})

        response = self.client.put(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)
        self.assertEqual(response.json, '')
        self.assertEqual(response.status_code, 200)

    def test_put_items_has_wrong_field(self):
        payload = copy.deepcopy(self.mock_items['campo_errado_put'])
        payload_post = json.dumps({'content': [self.mock_items['valido']]})

        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload_post)

        id = response.json['content'][0]
        payload['_id'] = id
        payload = json.dumps({'content': [payload]})
        response_put = self.client.put(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)

        for key, value in response_put.json['error'].items():
            if isinstance(value, list):
                for message in value:
                    self.assertEqual('Unknown field.', message)

    def test_put_items_has_not_required_fields(self):
        payload_post = json.dumps({'content': [self.mock_items['valido']]})

        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload_post)

        payload = copy.deepcopy(self.mock_items['sem_obrigatorios'])
        id = response.json['content'][0]
        payload['_id'] = id
        payload = json.dumps({'content': [payload]})
        response_put = self.client.put(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)
        for key, value in response_put.json['error'].items():
            if isinstance(value, list):
                for message in value:
                    self.assertEqual(
                        'Missing data for required field.', message)

    def test_put_items_has_invalid_id(self):
        payload = copy.deepcopy(self.mock_items['invalido_id'])

        payload = json.dumps({'content': [payload]})

        response = self.client.put(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid ID', response.json['error'][0]['0'])

    def test_put_items_has_nonexistent_id(self):
        payload = copy.deepcopy(self.mock_items['inexistente_id'])
        payload = json.dumps({'content': [payload]})

        response = self.client.put(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('Nonexistent ID', response.json['error'][0]['0'])

    # PATCH
    def test_patch_items_has_empty_body(self):
        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload_post)

        payload = copy.deepcopy(self.mock_items['valido_patch'])
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
        payload = self.mock_items['invalido_id']
        payload = json.dumps({'content': [payload]})

        response = self.client.patch(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid ID', response.json['error'][0]['0'])

    def test_patch_items_has_nonexistent_id(self):
        payload = self.mock_items['inexistente_id']
        payload = json.dumps({'content': [payload]})

        response = self.client.patch(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('Nonexistent ID', response.json['error'][0]['0'])
