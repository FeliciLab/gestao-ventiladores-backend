import json
from tests.base_case import BaseCase


class TestItemsMerge(BaseCase):
    def many_merge_post(self, mock):
        payload = json.dumps(mock)

        response = self.client.post(
            "/v2/items/merge",
            headers={"Content-Type": "application/json"},
            data=payload,
        )

        return response

    def process_bad_request(self, mock_key, message):
        response = self.many_merge_post(self.get_mock("item", mock_key))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["error"], message)

    def test_no_field_toUpdate_returns_status_400(self):
        self.process_bad_request(
            "itens_merge_sem_toUpdate", "Requisição sem campo toUpdate."
        )

    def test_field_toUpdate_empty_returns_status_400(self):
        self.process_bad_request(
            "itens_merge_com_toUpdate_vazio",
            "Campo toUpdate não pode ser objeto vazio.",
        )

    def test_no_field_toRemove_returns_status_400(self):
        self.process_bad_request(
            "itens_merge_sem_toRemove", "Requisição sem campo toRemove."
        )

    def test_empty_list_in_toRemove_returns_status_400(self):
        self.process_bad_request(
            "lista_vazia_toRemove", "Campo toRemove não pode ser lista vazia."
        )

    def test_invalid_item_in_toUpdate_returns_status_400(self):
        pass

    def test_invalid_id_item_in_toRemove_returns_status_400(self):
        pass

    def test_inexistent_itens_in_toRemove_are_ignored(self):
        pass

    def test_valid_item_toUpdate_creates_new_item(self):
        pass

    def test_copy_item_id_of_toUpdatee_to_toRemove(self):
        pass

