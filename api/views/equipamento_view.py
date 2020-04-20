import json
from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from api.schemas import equipamento_schema
from api.services import equipamento_service
from bson.json_util import dumps


class EquipamentoList(Resource):
    def get(self):
        equipamentos = equipamento_service.listar_equipamentos()
        return Response(equipamentos, mimetype="application/json", status=200)

    def post(self):
        body = request.json

        # Verificar se o equipamento já existe?
        erro_equipamento = equipamento_schema.EquipamentoSchema().validate(body)
        if erro_equipamento:
            return make_response(jsonify(erro_equipamento), 400)

        equipamento_existente = equipamento_service.consultar_numero_de_serie(
            body["numero_de_serie"]
        )

        if equipamento_existente:
            return make_response(
                jsonify({
                    "error": True,
                    "message": "Número de série já cadastrado",
                    "equipamento": dumps(equipamento_existente)
                }),
                400
            )

        novo_equipamento_id = equipamento_service.registar_equipamento(body)
        resposta = json.dumps({"_id": novo_equipamento_id})

        return Response(resposta, mimetype="application/json", status=201)


class EquipamentoDetail(Resource):
    def get(self, _id):
        equipamento = equipamento_service.listar_equipamento_by_id(_id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrada..."), 404)
        return Response(equipamento, mimetype="application/json", status=200)

    def put(self, _id):
        equipamento = equipamento_service.listar_equipamento_by_id(_id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrada..."), 404)

        body = request.get_json()
        erro_equipamento = equipamento_schema.EquipamentoSchema().validate(body)
        if erro_equipamento:
            return make_response(jsonify(erro_equipamento), 400)

        equipamento_service.atualizar_equipamento(body, _id)
        equipamento_atualizado = equipamento_service.listar_equipamento_by_id(_id)
        return Response(equipamento_atualizado, mimetype="application/json", status=200)

    def delete(self, _id):
        equipamento = equipamento_service.listar_equipamento_by_id(_id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrado..."), 404)
        equipamento_service.deletar_equipamento(_id)
        return make_response('', 204)

