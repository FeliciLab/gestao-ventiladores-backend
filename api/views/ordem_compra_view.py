from flask import Response, request, make_response, jsonify
from flask_restful import Resource
#from ..schemas import ordem_compra_schema
from ..services import ordem_compra_service

class NumeroOrdemServicoList(Resource):
    def post(self):
        """ Cadastra uma nova ordem compra """
        body = request.json
        ordem_compra_registrada = ordem_compra_service.registar_ordem_compra(body).to_json()
        return Response(ordem_compra_registrada, mimetype="application/json", status=201)