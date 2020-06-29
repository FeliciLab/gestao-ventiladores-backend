import json
from run import app
from unittest import TestCase
from mockito import when, mock
from ...mocks.mock_service_orders import mock_service_orders
from api.v2.models.schemas.service_order_schema import ServiceOrderSchema
from http import HTTPStatus


class ServiceOrdersSchema(TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_body_with_id_returns_error(self):
        erro_schema = (False, "Id must not be sent")
        when(ServiceOrderSchema).validate_save(
            mock_service_orders["service_order_with_id"]
        ).thenReturn(erro_schema)

        payload = json.dumps(
            {"content": [mock_service_orders["service_order_with_id"]]}
        )

        response = self.client.post(
            "/v2/service_orders",
            headers={"Content-Type": "application/json"},
            data=payload,
        )

        error = response.json
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertIn("error", error)
        self.assertEqual(type(error["error"]), list)
        self.assertIn("0", error["error"][0])
        self.assertEqual(error["error"][0]["0"], "Id must not be sent")

    def test_body_with_updated_returns_error(self):
        erro_schema = (False, "Updated must not be sent")
        when(ServiceOrderSchema).validate_save(
            mock_service_orders["service_order_with_updated"]
        ).thenReturn(erro_schema)

        payload = json.dumps(
            {"content": [mock_service_orders["service_order_with_updated"]]}
        )

        response = self.client.post(
            "/v2/service_orders",
            headers={"Content-Type": "application/json"},
            data=payload,
        )

        error = response.json
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertIn("error", error)
        self.assertEqual(type(error["error"]), list)
        self.assertIn("0", error["error"][0])
        self.assertEqual(error["error"][0]["0"], "Updated must not be sent")

    def test_body_with_deleted_returns_error(self):
        erro_schema = (False, "Deleted must not be sent")
        when(ServiceOrderSchema).validate_save(
            mock_service_orders["service_order_with_deleted"]
        ).thenReturn(erro_schema)

        payload = json.dumps(
            {"content": [mock_service_orders["service_order_with_deleted"]]}
        )

        response = self.client.post(
            "/v2/service_orders",
            headers={"Content-Type": "application/json"},
            data=payload,
        )

        error = response.json
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertIn("error", error)
        self.assertEqual(type(error["error"]), list)
        self.assertIn("0", error["error"][0])
        self.assertEqual(error["error"][0]["0"], "Deleted must not be sent")
