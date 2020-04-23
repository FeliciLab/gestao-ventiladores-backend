from importlib.resources import Resource

from flask import Response, request, make_response, jsonify

from api.services import movimentacao_service


class MovimentacaoList(Resource):
    def get(self):
        movimentacao = movimentacao_service.listar_movimentacoes()
        return Response(movimentacao.to_json(), mimetype="application/json", status=200)

    def post(self):
        body = request.json
        movimentacao_cadastrada = movimentacao_service.listar_fmovimentacao_id(body["id"])
        if movimentacao_cadastrada:
            return make_response(jsonify("Movimentação já cadastrada..."), 403)
        movimentacao_validacao = movimentacao_schema.MovimentacaoSchema().validate(request.json)
        if movimentacao_validacao:
            return make_response(jsonify(movimentacao_validacao), 400)
        validacao_marca = fabricante_schema.MarcaSchema()
        for marca in request.json['marcas']:
            if validacao_marca.validate(marca):
                return make_response(jsonify(validacao_marca), 400)
        fabricante_registrado = fabricante_service.registar_fabricante(body)
        return Response(fabricante_registrado, mimetype="application/json", status=201)


class MovimentacaoDetail(Resource):
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


class MovimentacaoQuery(Resource):
    pass