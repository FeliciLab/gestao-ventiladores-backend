from api.v2.services.item_service import ItemService
import api.v2.repositories.service_order_repository as service_order_repository
from api.v2.services.service_order_service import ServiceOrderService
from api.v2.utils.service_order_util import (has_accessories_service_order, has_items_service_order)


def create_new_item_from_to_update(item):
    return ItemService().register_item(item)


def handle_update_service_order(service_order, items_to_remove, new_item_id):
    to_update = False

    for item_to_remove in items_to_remove:
        if has_items_service_order(service_order):
            for i in range(len(service_order['diagnostico']['itens'])):
                item = service_order['diagnostico']['itens'][i]
                if item["item_id"] == item_to_remove:
                    item["item_id"] = new_item_id
                    service_order['diagnostico']['itens'][i] = item
                    to_update = True

        if has_accessories_service_order(service_order):
            for i in range(len(service_order['triagem']['acessorios'])):
                item = service_order['triagem']['acessorios'][i]
                if item["item_id"] == item_to_remove:
                    item["item_id"] = new_item_id
                    service_order['triagem']['acessorios'][i] = item
                    to_update = True

    return to_update, service_order


def delete_items_to_remove(to_remove):
    for item_id in to_remove:
        ItemService().delete_item(item_id)


def handle_removed_items(to_remove, new_item_id):
    ordens_servico = service_order_repository.fetch_all()
    for service_order in ordens_servico:
        to_update, data = handle_update_service_order(service_order, to_remove, new_item_id)
        if to_update:
            del data["_id"]
            ServiceOrderService().update(service_order["_id"], data)


def register_items(body):
    new_item_id = create_new_item_from_to_update(body["content"]["toUpdate"])
    handle_removed_items(body["content"]["toRemove"], new_item_id)
    delete_items_to_remove(body["content"]["toRemove"])
    return True, new_item_id
