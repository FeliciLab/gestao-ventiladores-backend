import json
from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from api.schemas import equipamento_schema
from api.services import equipamento_service
from bson.json_util import dumps

from api.utils.error_response import error_response


class EquipamentoCrud(Resource):
    def get(self):
        body = request.args
        try:
            _id = body['_id']
        except:
            _id = False

        if not _id:
            equipamentos = equipamento_service.listar_equipamentos()
            return Response(equipamentos.to_json(), mimetype="application/json", status=200)

        try:
            equipamento = equipamento_service.listar_equipamento_by_id(_id)
            return Response(equipamento.to_json(), mimetype="application/json", status=200)
        except:
            return error_response("Não foi possível encontrar equipamento com o parâmetro enviado")

    def post(self):
        body = request.json

        try:
            _id = body["_id"]
        except:
            _id = False

        erro_equipamento = equipamento_schema.EquipamentoSchema().validate(body)
        if erro_equipamento:
            return make_response(jsonify(erro_equipamento), 400)

        equipamento_existente = equipamento_service.consultar_numero_de_serie(
            body["numero_de_serie"]
        )

        if not _id and equipamento_existente:
            return make_response(
                jsonify({
                    "error": True,
                    "message": "Número de série já cadastrado",
                    "equipamento": dumps(equipamento_existente)
                }),
                400
            )

        if not _id:
            novo_equipamento_id = equipamento_service.registar_equipamento(body)
            resposta = json.dumps({"_id": novo_equipamento_id})
        else:
            equipamento_service.atualizar_equipamento(body, _id)
            resposta = json.dumps({"_id": _id})

        return Response(resposta, mimetype="application/json", status=200)

    def delete(self):
        body = request.args
        try:
            _id = body['_id']
        except:
            return error_response('Identificador não encontrado')

        try:
            equipamento = equipamento_service.listar_equipamento_by_id(_id)
            if equipamento is None:
                return error_response("Equipamento não encontrado.")
        except:
            return error_response("Não foi possível encontrar equipamento com o ID enviado.")

        equipamento_service.deletar_equipamento(_id)
        Response(jsonify({"ok": True}), mimetype="application/json", status=204)

class EquipamentoDetail(Resource):
    def get(self, _id):
        equipamento = equipamento_service.listar_equipamento_by_id(_id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrada..."), 404)
        return Response(equipamento, mimetype="application/json", status=200)

    def put(self, _id):
        equipamento = equipamento_service.listar_equipamento_by_id(_id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrada..."), 400)

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
            return make_response(jsonify("Equipamento não encontrado..."), 400)
        equipamento_service.deletar_equipamento(_id)
        return make_response('', 204)

