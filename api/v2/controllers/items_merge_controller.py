from flask_restful import Resource
from flask import request
from ..helpers.helper_response import error_response
from ..validation.validation_request import (
    validate_merge_items_request
)
from ..validation.schemas.item_schema import ItemSchema

class ItensMergeController(Resource):

    def post(self):
        body = request.get_json()
        validate, message = validate_merge_items_request(body)
        if not validate:
            return error_response(message)

        errors = {}

        errors_toUpdate = ItemSchema().validate(body["content"]["toUpdate"])
        if errors_toUpdate:
            errors['errors_toUpdate'] = errors_toUpdate

        errors_toRemove = {}
        for index, item in enumerate(body["content"]["toRemove"]):
            erro_schema = ItemSchema().validate(item)
            if erro_schema:
                errors_toRemove[str(index)] = erro_schema
        if errors_toRemove:
            errors['errors_toRemove'] = errors_toRemove

        if errors:
            return error_response(errors)

        return "", 201


