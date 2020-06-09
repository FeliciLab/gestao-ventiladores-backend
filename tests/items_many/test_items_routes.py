from tests.base_case import BaseCase
import json
import copy

class TestItemsRoutes(BaseCase):
    # GET testes
    def test_items_has_get_route(self):
        response = self.client.get('/v2/items')
        self.assertNotEqual(response.status_code, 405)

    def test_get_items_if_there_is_parameter_deleted_is_not_equal_true(self):
        response = self.client.get('/v2/items?deleted=errei_no_trampo')
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json)
        self.assertEqual(response.json["error"], "Parameter deleted is not equal true.")

    def test_get_items_if_there_is_parameter_deleted(self):
        response = self.client.get('/v2/items?deleted=true')
        self.assertEqual(response.status_code, 200)
        self.assertIn('deleted', response.json)
        self.assertEqual(response.json['deleted'], True)
    
    def test_get_items_if_there_is_not_parameter_deleted(self):
        response = self.client.get('/v2/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn('deleted', response.json)
        self.assertEqual(response.json['deleted'],False)

    # POST testes
    def test_items_has_post_route(self):
        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"})
        self.assertNotEqual(response.status_code, 405)
    
    def test_items_post_has_no_body(self):
        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 400)

    def test_items_post_has_empty_body(self):
        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=[])
        self.assertEqual(response.status_code, 400)

    def test_items_body_no_required_fields(self):
        payload = json.dumps({'content':[self.mock_items['sem_obrigatorios']]})
        response = self.client.post(
            '/v2/items',
            headers={"Content-Type": "application/json"},
            data=payload)
        self.assertEqual(response.status_code, 400)
    