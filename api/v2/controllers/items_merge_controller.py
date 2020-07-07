from flask_restful import Resource
from flask import request
from ..helpers.helper_response import error_response
from ..validation.validation_request import (
    validate_merge_items_request
)

class ItensMergeController(Resource):

    def post(self):
        body = request.get_json()
        validate, message = validate_merge_items_request(body)
        if not validate:
            return error_response(message)

        return "", 201


