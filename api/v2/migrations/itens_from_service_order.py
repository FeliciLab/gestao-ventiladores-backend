# 1 - Buscar na ordem de servico (triagem)
# 2 - Tratamento
# 3 - Inserir na collection Itens
# 4 - Remodelar ordem de serviço
# =========================================
from api.services.ordem_servico_service import listar_ordem_servico
from api.v2.services.item_service import ItemService
from slugify import slugify
from flask import request
from run import app
import json
import pandas as pd

# Adicionar rota
# Não deixar inserir nomes repetidos


class ItemsMigration():
    def fetch_items_from_triagem(self):
        service_orders = json.loads(listar_ordem_servico())
        items = {}

        # triagens = list(filter((lambda x: x['triagem'] if 'triagem' in x else None), service_orders))
        # acessorios = list(map((lambda x: x['acessorios'] if 'acessorios' in x else None), triagens))

        for service_order in service_orders:
            if 'triagem' in service_order:
                if 'acessorios' in service_order['triagem']:
                    for acessorio in service_order['triagem']['acessorios']:
                        reference_key = slugify(
                            acessorio['descricao'], separator='')
                        if not reference_key in items:
                            acessorio['reference_key'] = reference_key
                            items[reference_key] = acessorio
                            continue
                        items[reference_key]['quantidade'] += acessorio['quantidade']
        return items

    def format_items_names(self, items):
        for item in items:
            item['reference_key'] = slugify(item['descricao'], separator='')

        return items

    def group_items(self, items):
        df = pd.DataFrame(items)
        grouped = df.groupby(['reference_key', 'acompanha', 'descricao']).sum()
        grouped = grouped.reset_index().to_dict('records')

        # Escolher a descricao com o maior nome

        # new_itens = []

        # for item in grouped:
        #     aux = {}
        #     aux['refe...'] = formatado
        #     aux['nome'] = item['descricao']
        #     aux['quantidade'] = item['quantidade']
        #     aux['unidade_medida'] = 'und'

        #     new_itens.append(aux)

        return grouped

    def register_items(self, items):
        for item in items:
            ItemService().register_item(item)


items = ItemsMigration().fetch_items_from_triagem()
items = ItemsMigration().format_items_names(items)
items = ItemsMigration().group_items(items)
# ItemsMigration().register_items(items)
