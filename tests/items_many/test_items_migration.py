import ipdb; ipdb.set_trace()
from tests.base_case import BaseCase
from ...api.v2.migrations.itens_from_service_order import ItemsMigration


class TestItemsMigration(BaseCase):
    def test_items_from_triagem(self):
        response = ItemsMigration().fetch_items_from_triagem()
        self.assertEqual(type(response), list)

    def test_items_has_formatted_names(self):
        pass

