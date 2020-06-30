from flask_restful import Resource
from flask import make_response, jsonify, request
from .items_from_triagem_service_order import ItemsTriagemMigration
from .items_from_diagnostico_service_order import ItemsDiagnosticoMigration
from api.v2.services.item_service import ItemService


class ItemsMigrationBase(Resource):
    def get(self):
        self.register_items('triagem')
        self.register_items('diagnostico')

        return make_response(jsonify('Items migrated.'), 200)

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
