from flask_restful import Resource
from flask import make_response, jsonify, request
from ..helpers.helper_response import error_response, get_response, post_response
from ..services.item_service import ItemService
from ..validation.schemas.item_schema import ItemSchema
from ..validation.validation_request import validate_post, invalid_deleted_parameter
import json

class ItemsManyController(Resource):
    def get(self):
        args_deleted = request.args.get('deleted')
        if invalid_deleted_parameter(args_deleted):
            return error_response("Parameter deleted is not equal true.", 400)

        content = ItemService().fetch_items_list(args_deleted)

        return get_response(content, args_deleted)
    

    def post(self):
        body = request.get_json()
        validate, message = validate_post(body)
        
        if not validate:
            return error_response(message)
    
        content = []
        for item in body['content']:
            erro_ = ItemSchema().validate(item)
            if erro_: 
                return error_response(f"Error on item {body['content'].index(item)}. {erro_}")
            
            content.append(ItemService().register_item(item))


        return post_response(content)


    def put(self):
        return {}
