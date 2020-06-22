from tests.base_case import BaseCase
from api.v2.migrations.items_from_diagnostico_service_order import ItemsDiagnosticoMigration

class TestItemsDiagnosticoMigration(BaseCase):

    def setUp(self):
        super(TestItemsDiagnosticoMigration, self).setUp()
        self.items_from_diagnostico = ItemsDiagnosticoMigration().fetch_items_from_diagnostico()

    def test_items_from_diagnostico_is_non_empty_list(self):
        response = self.items_from_diagnostico
        self.assertTrue(len(response) > 0)

    def test_item_should_generate_reference_key(self):
        item_diagnostico = self.get_mock("item", "diagnostico") 
        generated_reference_key = ItemsDiagnosticoMigration().generate_reference_key(item_diagnostico)
        self.assertEqual(generated_reference_key, "mangueirapu6mm")

    def test_object_is_valid_item(self):
        item_diagnostico = self.get_mock("item", "diagnostico_formatado") 
        generated_item = ItemsDiagnosticoMigration().generate_item(item_diagnostico)
        self.assertIn('nome', generated_item[0])
        self.assertIn('quantidade', generated_item[0])
        self.assertIn('unidade_medida', generated_item[0])
        self.assertIn('reference_key', generated_item[0])
