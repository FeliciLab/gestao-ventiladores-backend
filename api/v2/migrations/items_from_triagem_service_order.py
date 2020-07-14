from api.services.ordem_servico_service import listar_ordem_servico
from api.v2.services.item_service import ItemService
from slugify import slugify

import json


class ItemsTriagemMigration():
    def fetch_items_from_triagem(self):
        service_orders = json.loads(listar_ordem_servico())
        items = {}

        for service_order in service_orders:
            if 'triagem' in service_order:
                if 'acessorios' in service_order['triagem']:
                    for acessorio in service_order['triagem']['acessorios']:
                        if "item_id" in acessorio:
                            continue

                        reference_key = self.generate_reference_key(acessorio)
                        acessorio['reference_key'] = reference_key
                        if not reference_key in items:
                            items[reference_key] = acessorio
                            continue

                        items[reference_key]['quantidade'] += acessorio[
                            'quantidade']
        return items

    def generate_reference_key(self, acessorio):
        return slugify(acessorio['descricao'], separator='')

    def generate_item(self, items):
        new_items = []

        for key, item in items.items():
            aux = {}
            aux['tipo'] = 'acessorio'
            aux['nome'] = item['descricao']
            aux['quantidade'] = item['quantidade']
            aux['unidade_medida'] = 'und'
            aux['reference_key'] = item['reference_key']
            new_items.append(aux)

        return new_items

    def get_items(self):
        items_from_collection = self.fetch_items_from_triagem()
        items = self.generate_item(items_from_collection)

        return items
