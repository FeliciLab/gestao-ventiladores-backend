from tests.base_case import BaseCase
from mockito import when, mock
from http import HTTPStatus
import io
import json


class TestImagesRoute(BaseCase):
    def access_route(self, id):
        route = f'/v2/service_order/{id}/foto_antes_limpeza.jpg'
        response_get = self.client.get(route)
        return response_get

    def test_route_exists(self):
        response = self.access_route('123')
        self.assertNotEqual(response.status_code, 405)

    def test_image_exists(self):
        response = access_route('123')
        self.assertEqual(response.status_code, 200)

    def test_image_not_exists(self):
        response = self.access_route('4002')
        self.assertEqual(response.status_code, 404)
