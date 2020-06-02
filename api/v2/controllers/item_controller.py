from flask_restful import Resource
from flask import jsonify, request
import json
from ..services.item_service import ItemService


class ItemMany(Resource):
    def get(self):
        args_deleted = request.args.get('deleted')
        if args_deleted:
            items_mongo = ItemService().list_items(deleted=True)
        else:
            items_mongo = ItemService().list_items()
        
        if items_mongo is None:
            return jsonify({"msg": "No items registered."}), 200
        
        items = json.loads(items_mongo.to_json())
        return jsonify(items), 200


# TODO essa classe items pode ser utiliza 
# class ItemOne(Resource):
#     def get(self, _id):
#         items_mongo = ItemService().list_item_by_id(_id)
        
#         if items_mongo is None:
#             return jsonify({"msg": "Item not found."}), 404
        
#         items = json.loads(items_mongo.to_json())
#         return jsonify(items), 200