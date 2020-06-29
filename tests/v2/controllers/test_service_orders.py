import json
from run import app
from unittest import TestCase
from mockito import when
from unittest.mock import MagicMock, patch
from api.v2.services.service_order_service import ServiceOrderService
from http import HTTPStatus
from .fixtures.service_orders import valid_service_order
from ..mocks.mock_service_orders import mock_service_orders
from bson.objectid import ObjectId


class ServiceOrdersController(TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_returns_service_orders_on_successful_request(self):
        service_orders = [{'equipamento_id': 1, 'numero_ordem_servico': '0400'}]
        when(ServiceOrderService).fetch_active().thenReturn(service_orders)

        response = self.client.get("/v2/service_orders")
api.add_resource(service_orders_many_controller.ServiceOrdersManyController, *[
        '/v2/service_orders/<int:id>',
        '/v2/service_orders',
    ])
        self.assertEqual(response.status_code, HTTPStatus.OK)
        content = response.json['content']
        self.assertEqual(type(content), list) 
        self.assertIn('content', response.json)
        self.assertIn('equipamento_id', content[0])
        self.assertEqual(content[0]['equipamento_id'], service_orders[0]['equipamento_id'])

    def test_get_returns_deleted_service_orders_on_successful_request(self):
        service_orders = [{'equipamento_id': 1, 'numero_ordem_servico': '0400'}]
        content = response.json["content"]
        self.assertEqual(type(content), list)
        self.assertIn("content", response.json)
        self.assertIn("equipamento_id", content[0])
        self.assertEqual(
            content[0]["equipamento_id"], service_orders[0]["equipamento_id"]
        )

    def test_returns_empty_list(self):
        service_orders = []
        when(ServiceOrderService).fetch_active().thenReturn(service_orders)

        response = self.client.get("/v2/service_orders")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json["content"], [])

    def test_get_return_invalid_param_error(self):
        response = self.client.get('/v2/service_orders?deleted=trueee')
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(response.json['error'], 'Parameter deleted is not equal true.')

    def test_patch_with_id(self):
        payload = json.dumps(valid_service_order())

        with patch.object(ServiceOrderService, 'update', return_value=None) as mock_method:
            service = ServiceOrderService()
            response = self.client.patch('/v2/service_orders', 
                    headers={"Content-Type": "application/json"},
                    data=payload)

        self.assertEqual(response.status_code, HTTPStatus.OK)

        mock_method.assert_called_with(valid_service_order()['content'])

        

    # POST tests
    def test_returns_list_with_the_saved_ids(self):
        service_order_id = "5ee37c19d86b6a8893d1a3a7"  # Fake Id
        when(ServiceOrderService).save_service_order(
            mock_service_orders["complete_to_mockito"]
        ).thenReturn(service_order_id)

        payload = json.dumps(
            {"content": [mock_service_orders["complete"]]}
        )

        response = self.client.post(
            "/v2/service_orders",
            headers={"Content-Type": "application/json"},
            data=payload,
        )

        self.assertEqual(type(response.json["content"]), list)
        for id in response.json["content"]:
            self.assertEqual(ObjectId.is_valid(id), True)
