from api.services.ordem_servico_service import listar_ordem_servico
from api.v2.services.item_service import ItemService
from slugify import slugify
from flask import request
from run import app
import json
import pandas as pd

class ItemsTriagemMigration():
    def fetch_items_from_triagem(self):

        """
        Refatorar funcao para dividir responsabilidades
        """
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
        
    def generate_item(self, item):
        pass 

    def group_items(self, items):
        df = pd.DataFrame(items)
        grouped = df.groupby(['reference_key', 'acompanha', 'descricao']).sum()
        grouped = grouped.reset_index().to_dict('records')

        return grouped

    def register_items(self, items):
        """
        LEMBRAR Garantir que ao fazer a requisicao novamente o dado sobre quantidade é somado
        """
        for item in items:
            ItemService().register_item(item)