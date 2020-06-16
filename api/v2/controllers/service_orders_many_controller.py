from flask_restful import Resource
from ..helpers.helper_response import get_response
from ..services.service_order_service import ServiceOrderService


class ServiceOrdersManyController(Resource):
    def get(self):
        service_orders = ServiceOrderService().fetch_all()

        return get_response(service_orders, False)
