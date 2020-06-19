from tests.base_case import BaseCase
from mockito import when, mock
from http import HTTPStatus
import io
import json


class TestImagesRoute(BaseCase):
    def test_route_exists(self):
        with open('tests/service_order/a.jpg', 'rb') as img:
            imgByteIO = io.BytesIO(bytes(img.read()))

        response_post = self.client.post('/api/importar/imagem',
                                    content_type='multipart/form-data',
                                    data={'foto_apos_limpeza': (
                                        imgByteIO, 'a.jpg')},
                                    follow_redirects=True)
        _id = response_post.json
        route = f'/v2/service_order/{_id}/{_id}_foto_apos_limpeza.jpg'
        response_get = self.client.get(route)
        import ipdb; ipdb.set_trace()
        self.assertNotEqual(response_get.status_code, 405)
