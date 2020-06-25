from unittest import TestCase
from api.v2.controllers.dtos.many_request import ManyRequest
from api.v2.controllers.dtos.service_orders_request import ServiceOrdersRequest
from unittest.mock import Mock

class ManyRequestTest(TestCase):
    def setUp(self):
        self.request = Mock()

        self.valid_request = Mock()
        self.valid_request.get_json.return_value = {"content": []}

        self.post_request = Mock()
        self.post_request.method = 'POST'

    def test_theres_no_error_when_receiving_list(self):
        many_request = ManyRequest(self.valid_request)
        many_request.validate()
        self.assertEqual(many_request.errors, [])
        self.assertEqual(many_request.valid, True)

    def test_with_a_contentless_request(self):
        self.request.get_json.return_value = {}

        many_request = ManyRequest(self.request)
        many_request.validate()

        self.assertEqual(many_request.errors, ['No content found'])
        self.assertEqual(many_request.valid, False)

    def test_has_error_when_not_list(self):
        invalid_request = Mock()
        invalid_request.get_json.return_value = {"content": {}}

        many_request = ManyRequest(invalid_request)
        many_request.validate()
        self.assertEqual(many_request.errors, ["Unexpected format. <class 'list'> was expected"])
        self.assertEqual(many_request.valid, False)

    def before_any_validation_is_done_it_is_not_valid(self):
        many_request = ManyRequest({})
        self.assertEqual(many_request.valid, None)

    def test_id_presence_validation_in_post_request(self):
        self.post_request.get_json.return_value = {"content": [{"_id": "xxx" }]}

        many_request = ManyRequest(self.post_request)
        many_request.validate()

        self.assertEqual(many_request.valid, False)
        self.assertEqual(many_request.errors, ['ID must not be sent'])