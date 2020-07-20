import unittest
from run import app

class EquipmentsControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.client = app.test_client()

    def test_response_has_content_list(self):
        response = self.client.get.json
        self.assertIn('content', response)
        self.assertIsInstance(response['content'], list)
