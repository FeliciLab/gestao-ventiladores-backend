from flask_restful import Resource
from ..helpers.helper_response import get_response
from ..services.service_order_service import ServiceOrderService
from flask import request

class ServiceOrdersManyController(Resource):
    def get(self):
        deleted_included = request.args.get("deleted")
        if deleted_included:
            service_orders = ServiceOrderService().fetch_all() 
        else:
            service_orders = ServiceOrderService().fetch_active()

        return get_response(service_orders, deleted_included)