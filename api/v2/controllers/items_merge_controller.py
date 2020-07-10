from flask_restful import Resource
from flask import request
import json
from ..helpers.helper_response import error_response
from .validators.validation_request import validate_merge_items_request
from ..services.item_service import ItemService
from ...services import ordem_servico_service
from bson.objectid import ObjectId
from api.models import ordem_servico_model



class ItemsMergeController(Resource):
    def post(self):
        body = request.get_json()
        validate, message = validate_merge_items_request(body)
        if not validate:
            return error_response(message)

        new_item_id = self.create_new_item_from_to_update(body["content"]["toUpdate"])

        ordens_servico = json.loads(ordem_servico_service.listar_ordem_servico())
        for item in body["content"]["toRemove"]:
            contains_item = self.check_if_service_order_has_item(item, ordens_servico)

            if(contains_item):
                self.save_items_to_remove(item)
                self.update_service_orders_with_object_id(contains_item, new_item_id)

        return "", 201

    def create_new_item_from_to_update(self, item):
        item_id = ItemService().register_item(item)
        return item_id

    def check_if_service_order_has_item(self, item, ordens_servico):
        contains_the_item = [service_order for service_order in ordens_servico if
                             item["_id"] == service_order["equipamento_id"]["$oid"]]
        if (contains_the_item):
            return contains_the_item
        return []

    def save_items_to_remove(self, item_to_remove):
        try:
            ItemService().delete_item(item_to_remove["_id"])
        except Exception:
            return "Não foi possível deletar o item com id: " + item_to_remove["_id"], 500
        return "Item Deletado", 200

    def update_service_orders_with_object_id(self, service_orders, new_object_id):
        for service_order in service_orders:
            #print(service_order["equipamento_id"])
            #print(new_object_id)
            #body = {"equipamento_id":  ObjectId(new_object_id)}
            body = {"numero_orderm_servico": "0002"}

            #{'set__': b'5f081a4ab1456b65512c1ac0'}

            #ordem_servico_model.OrdemServico.objects(id=service_order["_id"]).update(**query)

            print(service_order["_id"])
            new_service_order = service_order
            new_service_order["equipamento"]["_id"]["$oid"] = new_object_id
            updated_body = json.loads(
                ordem_servico_service.deserealize_ordem_servico(new_service_order).to_json())
            old_ordem_servico_body = json.loads(
                 ordem_servico_service.listar_ordem_servico_by_id(service_order["_id"]).to_json())
            ordem_servico_service.atualiza_somente_campos_repassados(service_order["_id"]["$oid"], body)

