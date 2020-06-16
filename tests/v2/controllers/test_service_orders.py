import json
from run import app
from unittest import TestCase
from mockito import when, mock
from api.v2.services.service_order_service import ServiceOrderService


class ServiceOrdersController(TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_returns_service_orders_on_successful_request(self):
        service_orders = [{'equipamento_id': 1, 'numero_ordem_servico': '0400'}]
        when(ServiceOrderService).fetch_all().thenReturn(service_orders)

        response = self.client.get('/v2/service_orders')
        HTTP_SUCCESS = 200
        self.assertEqual(response.status_code, HTTP_SUCCESS)
        content = response.json['content']

        self.assertEqual(type(content), list)
        self.assertIn('content', response.json)
        self.assertIn('equipamento_id', content[0])
        self.assertEqual(content[0]['equipamento_id'], service_orders[0]['equipamento_id'])


    def test_returns_empty_list(self):
        service_orders = []
        when(ServiceOrderService).fetch_all().thenReturn(service_orders)

        response = self.client.get('/v2/service_orders')
        HTTP_SUCCESS = 200
        self.assertEqual(response.status_code, HTTP_SUCCESS)
        content = response.json['content']

        self.assertEqual(content, [])
