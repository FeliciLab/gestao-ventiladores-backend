from unittest import TestCase
from api.v2.controllers.dtos.one_request import OneRequest
from unittest.mock import Mock

class OneRequestTest(TestCase):
    def setUp(self):
        self.request = Mock()

        self.valid_request = Mock()
        self.valid_request.get_json.return_value = {"content": {}}

        self.post_request = Mock()
        self.post_request.method = 'POST'

    def test_theres_error_when_receiving_list(self):
        many_request = OneRequest(self.valid_request)
        many_request.validate()

        self.assertEqual(many_request.errors, ["Unexpected format. <class 'dict'> was expected"])
        self.assertEqual(many_request.valid, False)

    def test_theres_no_error_when_receiving_dict(self):
        invalid_request = Mock()
        invalid_request.get_json.return_value = {"content": {}}

        many_request = OneRequest(invalid_request)
        many_request.validate()

        self.assertEqual(many_request.errors, [])
        self.assertEqual(many_request.valid, True)