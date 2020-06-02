from flask_restful import Resource
from flask import jsonify, request
import json

from ..helpers.error_response import error_response
from ..services.item_service import ItemService


def valid_deleted_paremeter(param):
    return param == "true"

class ItemsManyController(Resource):
    def get(self):
        args_deleted = request.args.get('deleted')
        if not valid_deleted_paremeter(args_deleted):
            return error_response("Parameter deleted is not equal true.", 400)

        pass
        #
        # if items_mongo is None:
        #     return jsonify({"msg": "No items registered."}), 200
        #
        # items = json.loads(items_mongo.to_json())
        # return jsonify(items), 200
