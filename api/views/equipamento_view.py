import json
from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from api.schemas import equipamento_schema
from api.services import equipamento_service, log_service
from bson.json_util import dumps
from api.utils.error_response import error_response
from flasgger import swag_from


class EquipamentoList(Resource):
    @swag_from('../../documentacao/equipamento/equipamentos_get.yml')
    def get(self):
        body = request.args
        try:
            _id = body['_id']
        except Exception:
            _id = False

        if not _id:
            equipamentos = equipamento_service.listar_equipamentos()
            return Response(equipamentos.to_json(),
                            mimetype="application/json",
                            status=200)

        try:
            equipamento = equipamento_service.listar_equipamento_by_id(_id)
            return Response(equipamento.to_json(),
                            mimetype="application/json",
                            status=200)
        except Exception:
            return error_response("Não foi possível encontrar" +
                                  "equipamento com o parâmetro enviado")

    @swag_from('../../documentacao/equipamento/equipamentos_post.yml')
    def post(self):
        body = request.json

        try:
            _id = body["_id"]
        except Exception:
            _id = False

        erro_equipamento = equipamento_schema \
            .EquipamentoSchema() \
            .validate(body)
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
            novo_equipamento_id = equipamento_service \
                .registar_equipamento(body)
            resposta = json.dumps({"_id": novo_equipamento_id})
        else:

            updated_body = json.loads(
                equipamento_service.deserealize_equipamento(body).to_json())
            old_body = json.loads(
                equipamento_service.listar_equipamento_by_id(_id).to_json())
            log_service.registerLog("equipamento",
                                    old_body,
                                    updated_body,
                                    ignored_fields=["created_at",
                                                    "updated_at"],
                                    all_fields=False)

            try:
                del body["_id"]
            except KeyError:
                print("_id não está presente no body")

            equipamento_service.atualizar_equipamento(body, _id)
            resposta = json.dumps({"_id": _id})

        return Response(resposta, mimetype="application/json", status=200)

    # @swag_from('../../documentacao/equipamento/equipamento_delete_body.yml')
    def delete(self):
        body = request.args
        try:
            _id = body['_id']
        except Exception:
            return error_response('Identificador não encontrado')

        try:
            equipamento = equipamento_service.listar_equipamento_by_id(_id)
            if equipamento is None:
                return error_response("Equipamento não encontrado.")
        except Exception:
            return error_response("Não foi possível encontrar " +
                                  "equipamento com o ID enviado.")

        equipamento_service.deletar_equipamento(_id)
        Response(jsonify({"ok": True}),
                 mimetype="application/json",
                 status=204)


class EquipamentoDetail(Resource):
    @swag_from('../../documentacao/equipamento/equipamento_get.yml')
    def get(self, _id):
        equipamento = equipamento_service.listar_equipamento_by_id(_id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrado..."), 404)

        return Response(
            equipamento.to_json(),
            mimetype="application/json",
            status=200
        )

    @swag_from('../../documentacao/equipamento/equipamento_put.yml')
    def put(self, _id):
        equipamento = equipamento_service.listar_equipamento_by_id(_id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrada..."), 400)

        body = request.get_json()
        erro_equipamento = equipamento_schema\
            .EquipamentoSchema().validate(body)
        if erro_equipamento:
            return make_response(jsonify(erro_equipamento), 400)

        updated_body = json.loads(
            equipamento_service.deserealize_equipamento(body).to_json())
        old_body = json.loads(
            equipamento_service.listar_equipamento_by_id(_id).to_json())
        log_service.registerLog("equipamento",
                                old_body,
                                updated_body,
                                ignored_fields=["created_at", "updated_at"],
                                all_fields=False)

        equipamento_service.atualizar_equipamento(body, _id)
        equipamento_atualizado = equipamento_service \
            .listar_equipamento_by_id(_id)

        return Response(equipamento_atualizado.to_json(),
                        mimetype="application/json",
                        status=200)

    @swag_from('../../documentacao/equipamento/equipamento_delete.yml')
    def delete(self, _id):
        equipamento = equipamento_service.listar_equipamento_by_id(_id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrado..."), 400)
        equipamento_service.deletar_equipamento(_id)
        return make_response('', 204)


class EquipamentoBulk(Resource):
    def post(self):
        body = request.json
        if 'equipamentos' not in body:
            return error_response('Equipamentos não enviado')

        a = []
        # agora vai
        for equipamento in body['equipamentos']:
            b = upsert_equipment(equipamento)
            if b is not False:
                a.append(b)

        return jsonify({"equipamentos": a})


def upsert_equipment(body):
    try:
        _id = body["_id"]
    except Exception:
        _id = False

    erro_equipamento = equipamento_schema.EquipamentoSchema().validate(body)
    if erro_equipamento:
        return False

    equipamento_existente = equipamento_service.consultar_numero_de_serie(
        body["numero_de_serie"]
    )

    if not _id and equipamento_existente:
        return False

    if not _id:
        novo_equipamento_id = equipamento_service \
            .registar_equipamento_complete(body)
        return json.loads(novo_equipamento_id.to_json())

    try:
        del body["_id"]
    except KeyError:
        print("_id não está presente no body")

    equipamento_service.atualizar_equipamento(body, _id)
    return json.loads(
        equipamento_service.listar_equipamento_by_id(_id).to_json())
