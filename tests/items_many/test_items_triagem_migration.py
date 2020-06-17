from tests.base_case import BaseCase
from api.v2.migrations.items_from_triagem_service_order import ItemsTriagemMigration

class TestItemsTriagemMigration(BaseCase):

    def setUp(self):
        super(TestItemsTriagemMigration, self).setUp()
        self.items_from_triagem = ItemsTriagemMigration().fetch_items_from_triagem()

    def test_items_from_triagem_is_dict(self):
        response = self.items_from_triagem
        self.assertEqual(type(self.items_from_triagem), dict)

    def test_items_from_triagem_is_non_empty_list(self):
        response = self.items_from_triagem
        self.assertTrue(len(response) > 0)

    def test_item_should_generate_reference_key(self):
        item_triagem = self.get_mock("item", "triagem_um") 
        generated_reference_key = ItemsTriagemMigration().generate_reference_key(item_triagem)
        self.assertEqual(generated_reference_key, "mangueiradeoxigenioverde")

    def test_object_is_valid_item(self):
        item_triagem = self.get_mock("item", "triagem_formatado") 
        generated_item = ItemsTriagemMigration().generate_item(item_triagem)
        self.assertIn('nome', generated_item[0])
        self.assertIn('quantidade', generated_item[0])
        self.assertIn('unidade_medida', generated_item[0])
        self.assertIn('reference_key', generated_item[0])

    def test_reference_key_in_collection(self):
        mock = self.get_mock("item","item_collection")
        response = self.many_make_post(mock)
        item_triagem = self.get_mock("item", "objeto_item")
        response = ItemsTriagemMigration().\
            check_reference_key_in_collection(item_triagem)
        self.assertEqual(response, False)
        
    def test_collection_items_should_have_one_key_per_name_of_item(self):
        pass

    
    
