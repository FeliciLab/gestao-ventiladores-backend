import json
from run import app
from unittest import TestCase


class ServiceOrdersController(TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_returns_service_orders_list(self):
        service_orders = [{'equipamento_id': 1, 'numero_ordem_servico': '0400'}]

        response = self.client.get('/v2/service_orders')
        content = response.json['content']
        HTTP_SUCCESS = 200

        self.assertEqual(response.status_code, HTTP_SUCCESS)
        self.assertEqual(type(content), list)
        self.assertIn('content', response.json)
        self.assertIn('equipamento_id', content[0])
        self.assertEqual(content[0]['equipamento_id'], service_orders[0]['equipamento_id'])
