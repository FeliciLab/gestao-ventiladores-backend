from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..schemas import fabricante_schema
from ..services import fabricante_service
from flasgger import swag_from

class FabricanteList(Resource):
    @swag_from('../../documentacao/fabricante/fabricantes_get.yml')
    def get(self):
        fabricantes = fabricante_service.listar_fabricantes()
        return Response(fabricantes, mimetype="application/json", status=200)

    @swag_from('../../documentacao/fabricante/fabricantes_post.yml')
    def post(self):
        body = request.json
        fabricante_cadastrado = fabricante_service.listar_fabricante_id(body["fabricante_nome"])
        if fabricante_cadastrado:
            return make_response(jsonify("Fabricante já cadastrado..."), 403)
        validacao_fabricante = fabricante_schema.FabricanteSchema().validate(request.json)
        if validacao_fabricante:
            return make_response(jsonify(validacao_fabricante), 400)
        validacao_marca = fabricante_schema.MarcaSchema()
        for marca in request.json['marcas']:
            if validacao_marca.validate(marca):
                return make_response(jsonify(validacao_marca), 400)
        fabricante_registrado = fabricante_service.registar_fabricante(body)
        return Response(fabricante_registrado, mimetype="application/json", status=201)

class FabricanteDetail(Resource):
    @swag_from('../../documentacao/fabricante/fabricante_put.yml')
    def put(self, fabricante_nome):
        body = request.get_json()
        fabricante_service.atualizar_fabricante(fabricante_nome, body)
        return '', 200

    @swag_from('../../documentacao/fabricante/fabricante_delete.yml')
    def delete(self, fabricante_nome):
        fabricante_service.deletar_fabricante(fabricante_nome)
        return '', 204

    @swag_from('../../documentacao/fabricante/fabricante_get.yml')
    def get(self, fabricante_nome):
        equipamento = fabricante_service.listar_fabricante_id(fabricante_nome)
        return Response(equipamento, mimetype="application/json", status=200)
