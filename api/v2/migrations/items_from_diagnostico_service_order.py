from api.v2.services.item_service import ItemService
from api.services.ordem_servico_service import listar_ordem_servico
from slugify import slugify
import json

class ItemsDiagnosticoMigration():
    def fetch_items_from_diagnostico(self):
        service_orders = json.loads(listar_ordem_servico())
        items = {}

        for service_order in service_orders:
            if 'diagnostico' in service_order.keys():
                if 'itens' in service_order['diagnostico']:
                    for item in service_order['diagnostico']['itens']:
                        reference_key = self.generate_reference_key(item)
                        if not reference_key in items:
                            item['reference_key'] = reference_key
                            items[reference_key] = item
                            continue
                        items[reference_key]['quantidade'] += item['quantidade']
        print(items)
        return items

    def generate_reference_key(self, item):
        reference_key = slugify(item['nome'], separator='')
        return reference_key

    def generate_item(self, items):
        new_items = []

        for key, item in items.items():
            new_items.append(item)

        return new_items

    def get_items(self):
        items_from_collection = self.fetch_items_from_diagnostico()
        items = self.generate_item(items_from_collection)
        
        return items
