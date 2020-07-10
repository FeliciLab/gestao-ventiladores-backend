import json
from tests.base_case import BaseCase
from mockito import when
from api.v2.services.item_service import ItemService
from api.v2.controllers.items_merge_controller import ItemsMergeController


class TestItemsMerge(BaseCase):
    def many_merge_post(self, mock):
        payload = json.dumps(mock)

        response = self.client.post(
            "/v2/items/merge",
            headers={"Content-Type": "application/json"},
            data=payload,
        )

        return response

    def mock_bad_request(self, mock_key, message):
        response = self.many_merge_post(self.get_mock("item", mock_key))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["error"], message)

    def test_no_field_toUpdate_returns_status_400(self):
        self.mock_bad_request(
            "itens_merge_sem_toUpdate", "Request without field toUpdate."
        )

    def test_field_toUpdate_empty_returns_status_400(self):
        self.mock_bad_request(
            "itens_merge_com_toUpdate_vazio",
            "Field toUpdate can't be empty object."
        )

    def test_no_field_toRemove_returns_status_400(self):
        self.mock_bad_request(
            "itens_merge_sem_toRemove", "Request without field toRemove."
        )

    def test_empty_list_in_toRemove_returns_status_400(self):
        self.mock_bad_request(
            "lista_vazia_toRemove", "Field toRemove can't be empty list."
        )

    def test_invalid_item_in_toUpdate_returns_status_400(self):
        message_marshmallow = {
            "toUpdate": {
                "codigo": ["Not a valid string."],
                "created_at": ["Not a valid datetime."],
                "descricao": ["Not a valid string."],
                "fabricante": ["Field may not be null."],
                "nome": ["Not a valid string."],
                "unidade_medida": ["Not a valid string."],
                "updated_at": ["Not a valid datetime."],
            }
        }
        self.mock_bad_request("item_invalido_em_toUpdate", message_marshmallow)

    def test_invalid_id_item_in_toRemove_returns_status_400(self):
        message_marshmallow = {
            "toRemove": {
                "0": {
                    "_id": ["Not a valid string."],
                    "codigo": ["Not a valid string."],
                    "created_at": ["Not a valid datetime."],
                    "descricao": ["Not a valid string."],
                    "fabricante": ["Field may not be null."],
                    "nome": ["Not a valid string."],
                    "unidade_medida": ["Not a valid string."],
                    "updated_at": ["Not a valid datetime."],
                }
            }
        }
        self.mock_bad_request("item_invalido_em_toRemove", message_marshmallow)

    def test_inexistent_items_in_toRemove_are_ignored(self):
        #item_inexistente = self.get_mock("item", "item_inexistente")
        #testar os métodos que vou implementar no controller
        #ItemsMergeController().merge_items([item_inexistente])
        #all_items = [] #substituir o all_items
        #when(ItemService).fetch_items_list().thenReturn(all_items)
        #all_items_ids = [item["_id"] for item in all_items]
        #self.assertNotIn(item_inexistente["_id"], all_items_ids)
        pass

    def test_valid_item_toUpdate_creates_new_item(self):
        pass

    def test_copy_item_id_of_toUpdate_to_toRemove(self):
        pass
