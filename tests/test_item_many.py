# Dado que Eu quero consultar todos os itens
# Quando efetuar o GET na rota /v2/items
# Então retornar uma lista com todos os dados de cada item salvo no banco, exceto os items que contenham o campo deleted_at

#  Dado que Eu quero consultar todos os itens, contendo os documentos removidos
# Quando efetuar o GET na rota /v2/items?deleted=true
# Então retornar uma lista com todos os dados de cada item salvo no banco, inclusive aqueles com o campo deleted_at

import sys
sys.path.append('..')
from base_case import BaseCase


class TestItemsMany(BaseCase):
    def test_exist_route_get_items(self):
        response = self.app.get('/v2/items')
        self.assertEqual(response.status_code, 200)

    def test_get_return_is_list(self):
        response = self.app.get('/v2/items')
        self.assertEqual(type(response.json), list)

    def test_get_items_return_body_list_without_deleted_at(self):
        items = self.app.get('/v2/items').json
        for item in items:
            self.assertEqual('deleted_at' in item.keys(), False)

    def test_get_items_deleted_return_body_list(self):
        items = self.app.get('/v2/items?deleted=true').json
        # Criar um item
        # Deletar um item
        # Retornar o item "deletado"
        for item in items:
            self.assertEqual('deleted_at' in item.keys(), True)

    def test_get_items_status_200(self):
        response = self.app.get('/v2/items')
        self.assertEqual(200, response.status_code)

    def test_get_items_empty_collection(self):
        pass

    def test_header_content_type_is_sent(self):
        pass

    def test_get_items_empty_collection(self):
        pass

    def test_header_content_type_is_sent(self):
        pass

    def test_item_many_has_get_method(self):
        pass

    def test_item_many_has_post_method(self):
        pass

    def test_item_many_has_put_method(self):
        pass

    def test_item_many_has_patch_method(self):
        pass

    def test_item_many_has_delete_method(self):
        pass

