from flask_restful import Resource
from flask import make_response, jsonify, request
from .items_from_triagem_service_order import ItemsTriagemMigration
from .items_from_diagnostico_service_order import ItemsDiagnosticoMigration
from api.v2.services.item_service import ItemService
from ..models import service_order_model
from ...services.ordem_servico_service import fetch_ordem_servico


def has_accessories_service_order(service_order):
    return "triagem" in service_order \
           and "acessorios" in service_order["triagem"]


def has_items_service_order(service_order):
    return "diagnostico" in service_order \
           and "itens" in service_order["diagnostico"]


def get_item_by_reference_key(items):
    doc = {}
    for item in items:
        doc[ItemsDiagnosticoMigration().generate_reference_key(item)] = item
    return doc


def define_service_order_screening(service_order, items):
    if has_accessories_service_order(service_order):
        for i in range(len(service_order["triagem"]["acessorios"])):
            acessorio = service_order["triagem"]["acessorios"][i]
            acessorio["item_id"] = items[ItemsTriagemMigration()
                .generate_reference_key(acessorio)]['_id']
            del acessorio['descricao']
            service_order["triagem"]["acessorios"][i] = acessorio

    return service_order


def define_service_order_diagnosis(service_order, items):
    if has_items_service_order(service_order):
        for i in range(len(service_order["diagnostico"]["itens"])):
            item = {}
            item["item_id"] = items[ItemsDiagnosticoMigration()
                .generate_reference_key(
                service_order["diagnostico"]["itens"][i]
            )]['_id']
            item['quantidade'] = service_order["diagnostico"]["itens"][i][
                'quantidade']
            service_order["diagnostico"]["itens"][i] = item

    return service_order


def update_service_order_migrated(service_order):
    id = service_order['_id']
    del service_order['_id']
    del service_order['equipamento']
    service_order_model.OrdemServico.objects.get(id=id).update(**service_order)


class ItemsMigrationBase(Resource):
    def handle_migrate_service_order(self):
        self.migrate_service_order(
            get_item_by_reference_key(ItemService().fetch_items_list()),
            fetch_ordem_servico()
        )

    def migrate_service_order(self, items, service_orders):
        for service_order in service_orders:
            update_service_order_migrated(
                define_service_order_diagnosis(
                    define_service_order_screening(service_order, items),
                    items
                )
            )

    def check_reference_key_in_collection(self, obj):
        items_from_collection = ItemService().fetch_items_list()

        for item in items_from_collection:
            if obj['reference_key'] in item.values():
                return False

        return True

    def register_items(self, key):
        items = []

        if key == 'triagem':
            items = ItemsTriagemMigration().get_items()

        elif key == 'diagnostico':
            items = ItemsDiagnosticoMigration().get_items()

        for item in items:
            validate = self.check_reference_key_in_collection(item)
            if validate:
                ItemService().register_item(item)

    def get(self):
        self.register_items('triagem')
        self.register_items('diagnostico')
        self.handle_migrate_service_order()

        return make_response(jsonify('Items migrated.'), 200)
