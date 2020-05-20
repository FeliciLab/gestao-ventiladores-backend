import json
from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..utils.error_response import error_response
from api.schemas import movimentacao_schema
from api.services import movimentacao_service, equipamento_service, log_service


class MovimentacaoList(Resource):
    def get(self):
        movimentacao_list = movimentacao_service.listar_movimentacoes()
        return Response(movimentacao_list,
                        mimetype="application/json",
                        status=200)

    # todo Refatorar esse metodo, muito codigo repetido by Lucas
    def post(self):
        body = request.json
        movimentacao_validacao = movimentacao_schema \
            .MovimentacaoSchema() \
            .validate(request.json)
        if movimentacao_validacao:
            return make_response(jsonify(movimentacao_validacao),
                                 400)

        response_status = None
        movimentacao_cadastrada = None
        _id = None

        if "_id" in body:
            _id = body["_id"]
            movimentacao_cadastrada = movimentacao_service \
                .listar_movimentacao_id(_id)

        if movimentacao_cadastrada:
            # todo sou obrigado a passar equipamento_id
            # na hora de atualizar com POST? by Denis
            equipamento_id_list = body["equipamentos_id"]
            equipamento_list = list()

            for equipamento_id in equipamento_id_list:
                equipamento = equipamento_service \
                    .listar_equipamento_by_id(equipamento_id)

                if equipamento is None:
                    return error_response("Equipamento " +
                                          equipamento_id +
                                          " inexistente")

                equipamento_list.append(equipamento)

            body["equipamentos_id"] = equipamento_list

            updated_body = json.loads(movimentacao_service
                                      .deserialize_movimentacao_service(body)
                                      .to_json())
            old_movimentacao_body = json.loads(
                movimentacao_cadastrada.to_json())

            log_service.registerLog("ordem_compra",
                                    old_movimentacao_body,
                                    updated_body,
                                    ["created_at", "updated_at"])

            del body["_id"]
            movimentacao_service.atualizar_movimentacao(_id, body)
            response_status = 200

        else:
            equipamento_id_list = body["equipamentos_id"]
            equipamento_list = list()

            for equipamento_id in equipamento_id_list:
                equipamento = equipamento_service \
                    .listar_equipamento_by_id(equipamento_id)

                if equipamento is None:
                    return error_response("Equipamento " +
                                          equipamento_id +
                                          " inexistente")

                equipamento_list.append(equipamento)

            body["equipamentos_id"] = equipamento_list

            movimentacao_cadastrada = movimentacao_service \
                .registar_movimentacao(body)
            _id = str(movimentacao_cadastrada.id)
            response_status = 201

        return Response(json.dumps({"_id": _id}),
                        mimetype="application/json",
                        status=response_status)


class MovimentacaoDetail(Resource):
    def put(self, _id):
        body = request.json
        movimentacao_validacao = movimentacao_schema \
            .MovimentacaoSchema() \
            .validate(request.json)

        if movimentacao_validacao:
            return make_response(jsonify(movimentacao_validacao), 400)

        movimentacao_cadastrada = movimentacao_service.listar_movimentacao_id(
            _id)

        if movimentacao_cadastrada is None:
            return Response("Movimentacao " +
                            str(_id) +
                            " inexistente",
                            mimetype="application/json",
                            status=200)

        if movimentacao_cadastrada:
            if "equipamentos_id" in body:
                equipamento_id_list = body["equipamentos_id"]
                equipamento_list = list()

                for equipamento_id in equipamento_id_list:
                    equipamento = equipamento_service \
                        .listar_equipamento_by_id(equipamento_id)

                    if equipamento is None:
                        return Response("Equipamento " +
                                        equipamento_id +
                                        " inexistente",
                                        mimetype="application/json",
                                        status=200)

                    equipamento_list.append(equipamento)

                if len(equipamento_list) != 0:
                    body["equipamentos_id"] = equipamento_list

            updated_body = json.loads(
                movimentacao_service.deserialize_movimentacao_service(body).to_json())
            old_movimentacao_body = json.loads(
                movimentacao_cadastrada.to_json())
            if len(updated_body['equipamentos_id']) == 0:
                del updated_body['equipamentos_id']

            log_service.registerLog("movimentacao",
                                    old_movimentacao_body,
                                    updated_body,
                                    ["codigo", "created_at", "updated_at"],
                                    all_fields=False)

            if "_id" in body:
                del body["_id"]

            movimentacao_service.atualizar_movimentacao(_id, body)

            return Response(json.dumps({"_id": _id}),
                            mimetype="application/json",
                            status=200)

    def get(self, _id):
        movimentacao = movimentacao_service.listar_movimentacao_id(_id)
        if movimentacao is not None:
            return Response(json.dumps({"_id": _id}),
                            mimetype="application/json",
                            status=200)

    def delete(self, _id):
        movimentacao_cadastrada = movimentacao_service.listar_movimentacao_id(
            _id)
        response = {"ok": False}
        if movimentacao_cadastrada is not None:
            movimentacao_service.deletar_movimentacao(_id)
            response = {"ok": True}

        return Response(json.dumps(response),
                        mimetype="application/json",
                        status=200)


class MovimentacaoQuery(Resource):
    def post(self):
        body = request.json
        dados_filtrados = movimentacao_service.movimentacao_queries(body)
        return Response(
            dados_filtrados,
            mimetype="application/json",
            status=200)
