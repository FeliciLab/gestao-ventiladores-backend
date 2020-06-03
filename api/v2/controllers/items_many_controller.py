from flask_restful import Resource
from flask import make_response, jsonify, request
import json
from ..helpers.error_response import error_response
from ..services.item_service import ItemService


def invalid_deleted_parameter(param):
    return param and param != "true"

class ItemsManyController(Resource):
    def get(self):
        args_deleted = request.args.get('deleted')
        if invalid_deleted_parameter(args_deleted):
            return error_response("Parameter deleted is not equal true.", 400)

        content = ItemService.fetch_items_list()

        response = {'content': content}

        response['deleted'] = True if args_deleted else False

        return make_response(jsonify(response), 200)
  