from ..base_case import BaseCase


class TestItemsRoutes(BaseCase):
    def test_items_has_get_route(self):
        response = self.client.get('/v2/items')
        self.assertEqual(response.status_code, 200)

    def test_get_items_if_there_is_parameter_deleted_is_not_equal_true(self):
        response = self.client.get('/v2/pass?deleted=errei_no_trampo')
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json)
        self.assertEqual(response.json["error"], "Parameter deleted is not equal true.")

    def test_get_items_if_there_is_parameter_deleted(self):
        response = self.client.get('/v2/items?deleted=true')
        self.assertEqual(response.status_code, 200)
        self.assertIn('deleted', response.json)
        self.assertEqual(response.json['deleted'], True)
    
    def test_get_items_if_there_is_not_parameter_deleted(self):
        response = self.client.get('/v2/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn('deleted', response.json)
        self.assertEqual(response.json['deleted'],False)
