from tests.base_case import BaseCase
from api.v2.migrations.items_migration_base import ItemsMigrationBase
from api.v2.migrations.items_from_triagem_service_order import ItemsTriagemMigration


class TestItemsBaseMigration(BaseCase):

    
    def test_reference_key_in_collection(self):
        mock = self.get_mock("item", "item_collection")
        response = self.many_make_post(mock)
        item_triagem = self.get_mock("item", "objeto_item")
        response = ItemsMigrationBase().\
            check_reference_key_in_collection(item_triagem)

        self.assertEqual(response, False)
