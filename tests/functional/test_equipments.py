import unittest
from run import app


class GetEquipmentTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        # Um client da api faz uma requisição para o endpoint /v2/equipments
        self.response = self.client.get('/v2/equipments')

    def test_endpoint_exists(self):
        # Ele recebe uma resposta indicando que o endpoint existe
        self.assertNotEqual(self.response.status_code, 404)

    def test_response_format(self):
        # E um payload com no formato json com uma chave 'content'
        self.assertIn('content', self.response.json)
        # cujo valor é uma lista
        self.assertIsInstance(self.response.json['content'], list)
