from tests.base_case import BaseCase


class TestItemsMigration(BaseCase):
    def test_items_from_triagem_is_list(self):
        response = self.items_from_triagem
        self.assertEqual(type(response), list)

    def test_items_from_triagem_is_non_empty_list(self):
        response = self.items_from_triagem
        self.assertTrue(len(response) > 0)

    def test_items_has_formatted_names(self):
        pass
