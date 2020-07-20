import unittest
from run import app


class GetEquipmentTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_endpoint_exists(self):
        # Um client da api faz uma requisição para o endpoint /v2/equipments
        response = self.client.get
        # Ele recebe uma resposta indicando que o endpoint existe
        self.assertNotEqual(response.status_code, 404)
