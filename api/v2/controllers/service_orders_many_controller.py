from flask_restful import Resource
from flask import make_response
from ..services.ordem_servico_service import listar_ordem_servico

class ServiceOrdersManyController(Resource):
    def get(self):
        service_orders = listar_ordem_servico()

        return make_response({'content': service_orders}, 200)