from flask_restful import Resource
from ..helpers.helper_response import get_response, error_response
from ..validation.validation_request import invalid_deleted_parameter
from ..services.service_order_service import ServiceOrderService
from http import HTTPStatus
from flask import request


class ServiceOrdersManyController(Resource):
    def get(self):
        deleted_included = request.args.get("deleted")
        if invalid_deleted_parameter(deleted_included):
            return error_response(
                "Parameter deleted is not equal true.", HTTPStatus.BAD_REQUEST)
        if deleted_included:
            service_orders = ServiceOrderService().fetch_all() 
        else:
            service_orders = ServiceOrderService().fetch_active()

        return get_response(service_orders, deleted_included)

    def post(self):

        return ''    
