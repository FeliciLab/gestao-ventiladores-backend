from api.services.ordem_servico_service import listar_ordem_servico
from api.v2.services.item_service import ItemService
from slugify import slugify
from flask_restful import Resource
from flask import make_response, jsonify
import json


class ItemsTriagemMigration(Resource):
    def fetch_items_from_triagem(self):
        service_orders = json.loads(listar_ordem_servico())
        items = {}

        for service_order in service_orders:
            if 'triagem' in service_order:
                if 'acessorios' in service_order['triagem']:
                    for acessorio in service_order['triagem']['acessorios']:
                        reference_key = self.generate_reference_key(acessorio)
                        if not reference_key in items:
                            acessorio['reference_key'] = reference_key
                            items[reference_key] = acessorio
                            continue
                        items[reference_key]['quantidade'] += acessorio['quantidade']
        return items

    def generate_reference_key(self, acessorio):
        reference_key = slugify(acessorio['descricao'], separator='')
        return reference_key

    def generate_item(self, items):
        new_items = []

        for key, item in items.items():
            aux = {}
            aux['nome'] = item['descricao']
            aux['quantidade'] = item['quantidade']
            aux['unidade_medida'] = 'und'
            aux['reference_key'] = item['reference_key']
            new_items.append(aux)

        return new_items

    def check_reference_key_in_collection(self, obj):
        items_from_collection = ItemService().fetch_items_list()

        for item in items_from_collection:
            if obj['reference_key'] in item.values():
                return False, item
        return True, ''

    def get_items(self):
        items_from_collection = self.fetch_items_from_triagem()
        items = self.generate_item(items_from_collection)
        
        return items

    def register_items(self):
        items = self.get_items()

        for item in items:
            validate, obj = self.check_reference_key_in_collection(item)
            if not validate:
                data = {'quantidade': item['quantidade']+obj['quantidade']}
                ItemService().update_item_only_fields(data, obj['_id'])
                continue
            ItemService().register_item(item)

    def get(self):
        self.register_items()
        
        return make_response(jsonify('Items migrated from triagem.'), 200)
