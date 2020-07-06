from tests.base_case import BaseCase

class TestItemsMerge(BaseCase):
    
    def test_no_field_toUpdate_returns_status_400(self):
        pass

    def test_no_field_toRemove_returns_status_400(self):
        pass

    def test_invalid_item_in_toUpdate_returns_status_400(self):
        pass

    def test_empty_list_in_toRemove_returns_status_400(self):
        pass

    def test_invalid_id_item_in_toRemove_returns_status_400(self):
        pass

    def test_inexistent_itens_in_toRemove_are_ignored(self):
        pass

    def test_valid_item_toUpdate_creates_new_item(self):
        pass

    def test_copy_item_id_of_toUpdatee_to_toRemove(self):
        pass

    