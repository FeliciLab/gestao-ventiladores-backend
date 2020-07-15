import json

from api.v2.services.item_merge_service import ItemsMergeService
from tests.base_case import BaseCase
from mongoengine.errors import ValidationError


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

    def test_invalid_item_in_toUpdate_raises_validation_error(self):
        body = self.get_mock("item", "item_invalido_em_toUpdate")
        items_merge_service = ItemsMergeService()
        self.assertRaises(ValidationError, items_merge_service.register_items, body)

    def test_invalid_id_item_in_toRemove_returns_status_400(self):
        message_marshmallow = {
            "toRemove": {
                "0000000000000000000000": "Invalid ID",
                "1111111111111111111111": "Invalid ID"
            }
        }
        self.mock_bad_request("item_invalido_em_toRemove", message_marshmallow)
