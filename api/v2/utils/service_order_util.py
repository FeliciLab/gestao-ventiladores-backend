def has_accessories_service_order(service_order):
    return "triagem" in service_order \
           and "acessorios" in service_order["triagem"]


def has_items_service_order(service_order):
    return "diagnostico" in service_order \
           and "itens" in service_order["diagnostico"]
