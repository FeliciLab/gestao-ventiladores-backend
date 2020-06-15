# 1 - Buscar na ordem de servico (triagem)
# 2 - Tratamento
# 3 - Inserir na collection Itens
# 4 - Remodelar ordem de serviço
# =========================================
from ...services.ordem_servico_service import listar_ordem_servico


class ItemsMigration():
    def fetch_items_from_triagem(self):
        service_orders = listar_ordem_servico()
        items = []

        triagens = list(filter((lambda x: x['triagem'] if 'triagem' in x else None), service_orders))
        acessorios = list(map((lambda x: x['acessorio'] if 'acessorio' in x else None), triagens))

        return acessorios

print(ItemsMigration().fetch_items_from_triagem())
