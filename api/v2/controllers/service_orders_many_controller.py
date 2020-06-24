from flask_restful import Resource
from ..helpers.helper_response import get_response
from ..validation.validation_request import invalid_deleted_parameter
from api.v2.controllers.validators.validation_request import validate_request
from api.v2.services.service_order_service import ServiceOrderService
from http import HTTPStatus
from flask import request
from api.v2.models.schemas.service_order_schema import ServiceOrderSchema
from api.v2.utils import error_response, success_response


class ServiceOrdersManyController(Resource):
    def get(self):
        deleted_included = request.args.get("deleted")
        if invalid_deleted_parameter(deleted_included):
            return error_response(
                "Parameter deleted is not equal true.", HTTPStatus.BAD_REQUEST
            )
        if deleted_included:
            service_orders = ServiceOrderService().fetch_all()
        else:
            service_orders = ServiceOrderService().fetch_active()

        return get_response(service_orders, deleted_included)

    def post(self):
        body = request.get_json()

        validate, message = validate_request(body)
        if not validate:
            return error_response(message)

        errors = []
        for index, service_order in enumerate(body["content"]):
            validate, message = ServiceOrderSchema().validate_post(service_order)
            if not validate:
                errors.append({index: message})
                continue

        if errors:
            return error_response(errors)

        # Testar se o id do item existe.

        content = []
        for service_order in body["content"]:
            content.append(ServiceOrderService().register_service_order(service_order))

        return success_response.post_response(content)
