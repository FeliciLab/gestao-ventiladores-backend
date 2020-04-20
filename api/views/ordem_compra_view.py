from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..schemas import ordem_compra_schema
from ..services import ordem_compra_service

class NumeroOrdemServicoList(Resource):
    def post(self):
        """ Cadastra uma nova ordem compra """
        body = request.json
        # validacao_fabricante = fabricante_schema.FabricanteSchema().validate(request.json)
        # if validacao_fabricante:
        #     return make_response(jsonify(validacao_fabricante), 400)
        # validacao_marca = fabricante_schema.MarcaSchema()
        ordem_compra_registrada = ordem_compra_service.registar_ordem_compra(body)
        return Response(ordem_compra_registrada, mimetype="application/json", status=201)