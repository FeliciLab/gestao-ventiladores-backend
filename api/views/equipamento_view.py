from flask import Response, request, make_response, jsonify
from flask_restful import Resource

from api.services import equipamento_service


class EquipamentoList(Resource):
    def get(self):
        equipamentos = equipamento_service.listar_equipamentos()
        return Response(equipamentos, mimetype="application/json", status=200)

    def post(self):
        body = request.json
        novo_equipamento = equipamento_service.registar_equipamento(body)
        return Response(novo_equipamento, mimetype="application/json", status=201)


class EquipamentoDetail(Resource):
    def get(self, _id):
        equipamento = equipamento_service.listar_equipamento(_id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrada..."), 404)
        return Response(equipamento, mimetype="application/json", status=200)

    def put(self, _id):
        equipamento = equipamento_service.listar_equipamento(_id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrada..."), 404)

        body = request.get_json()

        equipamento_service.atualizar_equipamento(body, _id)
        equipamento_atualizado = equipamento_service.listar_equipamento(_id)
        return Response(equipamento_atualizado, mimetype="application/json", status=200)

    def delete(self, _id):
        equipamento = equipamento_service.listar_equipamento(_id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrado..."), 404)
        equipamento_service.deletar_equipamento(_id)
        return make_response('', 204)
