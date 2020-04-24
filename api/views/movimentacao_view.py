import json

from flask import Response, request, make_response, jsonify
from flask_restful import Resource

from api.schemas import movimentacao_schema
from api.services import movimentacao_service, equipamento_service
from api.utils import query_parser

class MovimentacaoList(Resource):
    def get(self):
        movimentacao_list = movimentacao_service.listar_movimentacoes()
        movimentacao_id_list = list()

        for movimentacao in movimentacao_list:
            movimentacao_id_list.append({"_id": str(movimentacao.id)})

        return Response(str(movimentacao_id_list), mimetype="application/json", status=200)

    # todo Refatorar esse metodo, muito codigo repetido by Lucas
    def post(self):
        body = request.json
        movimentacao_validacao = movimentacao_schema.MovimentacaoSchema().validate(request.json)
        if movimentacao_validacao:
            return make_response(jsonify(movimentacao_validacao), 400)

        response_status = None
        movimentacao_cadastrada = None
        _id = None

        if "_id" in body:
            _id = body["_id"]
            movimentacao_cadastrada = movimentacao_service.listar_movimentacao_id(_id)

        if movimentacao_cadastrada:
            equipamento = equipamento_service.listar_equipamento_by_id(body["equipamento_id"])
            if equipamento is None:
                return Response("Equipamento inexistente", mimetype="application/json", status=200)

            body["equipamento_id"] = equipamento

            del body["_id"]

            movimentacao_service.atualizar_movimentacao(_id, body)
            response_status = 200
        else:
            equipamento = equipamento_service.listar_equipamento_by_id(body["equipamento_id"])
            if equipamento is None:
                return Response("Equipamento inexistente", mimetype="application/json", status=200)

            body["equipamento_id"] = equipamento

            movimentacao_cadastrada = movimentacao_service.registar_movimentacao(body)
            _id = str(movimentacao_cadastrada.id)
            response_status = 201

        return Response(json.dumps({"_id": _id}), mimetype="application/json", status=response_status)


class MovimentacaoDetail(Resource):
    def put(self, _id):
        body = request.json
        movimentacao_validacao = movimentacao_schema.MovimentacaoSchema().validate(request.json)

        if movimentacao_validacao:
            return make_response(jsonify(movimentacao_validacao), 400)

        if "_id" in body:
            del body["_id"]
        movimentacao_service.atualizar_movimentacao(_id, body)

        return Response(json.dumps({"_id": _id}), mimetype="application/json", status=200)

    def get(self, _id):
        movimentacao = movimentacao_service.listar_movimentacao_id(_id)
        if movimentacao is not None:
            return Response(json.dumps({"_id": _id}), mimetype="application/json", status=200)

    def delete(self, _id):
        movimentacao_cadastrada = movimentacao_service.listar_movimentacao_id(_id)
        response = {"ok": False}
        if movimentacao_cadastrada is not None:
            movimentacao_service.deletar_movimentacao(_id)
            response = {"ok": True}

        return Response(json.dumps(response), mimetype="application/json", status=200)


class MovimentacaoQuery(Resource):
    def post(self):
        body = request.json
        dados_filtrados = movimentacao_service.movimentacao_queries(body)
        return Response(dados_filtrados, mimetype="application/json", status=200)
