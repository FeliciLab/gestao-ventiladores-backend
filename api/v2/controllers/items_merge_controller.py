from flask_restful import Resource
from flask import request
from ..helpers.helper_response import error_response
from .validators.validation_request import validate_merge_items_request
from api.v2.services.item_merge_service import ItemsMergeService


class ItemsMergeController(Resource):
    def post(self):
        body = request.get_json()
        validate, message = validate_merge_items_request(body)

        if not validate:
            return error_response(message)

        merge_service = ItemsMergeService()
        validate, message = merge_service.register_items(body)
        if not validate:
            return error_response(message)

        return message, 201
