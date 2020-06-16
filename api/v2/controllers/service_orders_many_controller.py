from flask_restful import Resource
from flask import make_response
from ..services.service_order_service import ServiceOrderService


class ServiceOrdersManyController(Resource):
    def get(self):
        service_orders = ServiceOrderService().fetch_all()

        return make_response({'content': service_orders}, 200)
