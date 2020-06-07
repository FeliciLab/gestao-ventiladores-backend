from ..base_case import BaseCase
from bson import ObjectId
import json
import ipdb

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
    def test_put_items_has_json(self):
        payload = json.dumps({'content': [self.mock_items['valido']]})
        response = self.client.put(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)
        self.assertEqual(type(response.json), dict)

    def test_put_items_not_valid_body(self):
        post_correct = json.dumps({'content': [self.mock_items['valido']]})
        put_incorrect = self.mock_items['sem_obrigatorios']

        response_post = self.client.post(
        '/v2/items',
        headers={"Content-Type": "application/json"},
        data=post_correct)

        id = response_post.json['content'][0]
        put_incorrect['_id'] = id
        put_incorrect = json.dumps({'content': put_incorrect})

        response_put = self.client.put(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=put_incorrect)
        
        self.assertEqual(response_put.status_code, 400)
    
    def test_put_items_has_not_content_in_body(self):
        # payload_post = json.dumps({'somethind': [self.mock_items['invalido']]})
        pass


    def test_put_items_has_invalid_list_dict_items(self):
        # payload_post = json.dumps({'content': [self.mock_items['invalido']]})
        
        # id = response_post.json['content'][0]
        # payload_put = [id]

        # response = self.client.put(
        #     '/v2/items',
        #     headers={"Content-Type": "application/json"},
        #     data=payload_put)
        # self.assertEqual(response.status_code, 200)

        # self.assertEqual(type(response.json), dict)

        # def test_put_items_has_valid_id(self):
        #     payload = json.dumps({'content': [self.mock_items['valido']]})
        #     response = self.client.post(
        #         '/v2/items',
        #         headers={"Content-Type": "application/json"},
        #         data=payload)
        #     for _id in response.json['content']:
        #         str_id = ObjectId(_id)
        #         self.assertEqual(type(str_id), str)
        pass

