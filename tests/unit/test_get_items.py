# Dado que Eu quero consultar todos os itens
# Quando efetuar o GET na rota /v2/items
# Então retornar uma lista com todos os dados de cada item salvo no banco, exceto os items que contenham o campo deleted_at

#  Dado que Eu quero consultar todos os itens, contendo os documentos removidos
# Quando efetuar o GET na rota /v2/items?deleted=true
# Então retornar uma lista com todos os dados de cada item salvo no banco, inclusive aqueles com o campo deleted_at

import sys
sys.path.append('..')
from base_case import BaseCase


class TestGetItems(BaseCase):
    def test_exist_route_get_items(self):
        response = self.app.get('/v2/items')
        self.assertNotEqual(response.status_code, 404)

    def test_get_items_return_body_list(self):
        response = self.app.get('/v2/items')
        self.assertEqual(type(response.json), list)


    def test_get_items_return_body_list_without_deleted_at(self):
        items = self.app.get('/v2/items').json
        for item in items:
            self.assertEqual('deleted_at' in item.keys(), False)


    def test_get_items_deleted_return_body_list(self):
        items = self.app.get('/v2/items?deleted=true').json
        for item in items:
            self.assertEqual('deleted_at' in item.keys(), True)

    def test_get_items_status_200(self):
        response = self.app.get('/v2/items')
        self.assertEqual(200, response.status_code)
