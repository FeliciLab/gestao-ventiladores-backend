from flask_restful import Resource
from flask import jsonify, request
import json
from ..services.item_service import ItemService


class ItemMany(Resource):
    def get(self):
        args_route = request.args
        
        items_mongo = ItemService().list_items()
        if items_mongo is None:
            return jsonify({"msg": "No items registered."}, 200)
        
        items = json.loads(items_mongo.to_json())
        return jsonify(items, 200)
