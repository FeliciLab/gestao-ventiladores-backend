# Dado que Eu quero consultar todos os itens
# Quando efetuar o GET na rota /v2/items
# Então retornar uma lista com todos os dados de cada item salvo no banco, exceto os items que contenham o campo deleted_at

#  Dado que Eu quero consultar todos os itens, contendo os documentos removidos
# Quando efetuar o GET na rota /v2/items?deleted=true
# Então retornar uma lista com todos os dados de cada item salvo no banco, inclusive aqueles com o campo deleted_at

import sys
sys.path.append('..')
from base_case import BaseCase


class TestMiddleware(BaseCase):
    def test_header_content_type_is_sent(self):
        pass
