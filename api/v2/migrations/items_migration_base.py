from flask_restful import Resource
from flask import make_response, jsonify, request
from .items_from_triagem_service_order import ItemsTriagemMigration
from .items_from_diagnostico_service_order import ItemsDiagnosticoMigration
from api.v2.services.item_service import ItemService
from ...services.ordem_servico_service import listar_ordem_servico


class ItemsMigrationBase(Resource):
    def get(self):
        self.register_items('triagem')
        self.register_items('diagnostico')
        self.handle_migrate_service_order()

        return make_response(jsonify('Items migrated.'), 200)

    def get_item_by_reference_key(self, items):
        doc = {}
        for item in items:
            doc[item.reference_key] = item
        return doc

    def handle_migrate_service_order(self):
        self.migrate_service_order(
            self.get_item_by_reference_key(
                ItemService().fetch_items_list()
            ),
            listar_ordem_servico()
        )

    def migrate_service_order(self, items, service_orders):
        for service_order in service_orders:
            if "triagem" in service_order and "acessorios" in service_order["triagem"]:
                for i in  range(len(service_order["triagem"]["acessorios"])):
                    acessorio = service_order["triagem"]["acessorios"][i]
                    acessorio["item_id"] = items[ItemsTriagemMigration().generate_reference_key(acessorio)]._id
                    service_order["triagem"]["acessorios"][i] = acessorio

            if "diagnostico" in service_order and "itens" in service_order["diagnostico"]:
                for i in  range(len(service_order["diagnostico"]["itens"])):
                    item = service_order["diagnostico"]["itens"][i]
                    item["item_id"] = items[ItemsDiagnosticoMigration().generate_reference_key(item)]._id
                    service_order["diagnostico"]["itens"][i] = item


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


class ItemsMerge(Resource):
    def post(self):
        print(request.get_json())
        return 'joia'
