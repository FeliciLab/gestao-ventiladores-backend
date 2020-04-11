from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..models import fabricante_model
from ..schemas import fabricante_schema
from ..services import fabricante_service


class FabricanteList(Resource):
    def get(self):
        fabricantes = fabricante_service.listar_fabricantes()
        return Response(fabricantes, mimetype="application/json", status=200)

    def post(self):
        body = request.json
        fs = fabricante_schema.FabricanteSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            result =fabricante_service.registar_fabricante(body)
            return make_response(jsonify(result), 201)

class FabricanteDetail(Resource):
    def put(self, fabricante_nome):
        body = request.get_json()
        fabricante_service.atualizar_fabricante(fabricante_nome, body)
        return '', 200

    def delete(self, fabricante_nome):
        fabricante_service.deletar_fabricante(fabricante_nome)
        return '', 204

    def get(self, fabricante_nome):
        equipamento = fabricante_service.listar_fabricante_id(fabricante_nome)
        return Response(equipamento, mimetype="application/json", status=200)
