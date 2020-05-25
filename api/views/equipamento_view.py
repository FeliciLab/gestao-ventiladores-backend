import json
from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from api.schemas.equipamento_schema import EquipamentoSchema
from api.services import equipamento_service, log_service
from bson.json_util import dumps
from api.utils.error_response import error_response
from flasgger import swag_from


class EquipamentoMany(Resource):
    @swag_from('../../documentacao/equipamento/equipamento_get_many.yml')
    def get(self):
        equipamentos_json = equipamento_service.listar_equipamentos().to_json()
        equipamentos_dict = json.loads(equipamentos_json)
        return jsonify(equipamentos_dict)


    @swag_from('../../documentacao/equipamento/equipamento_post_many.yml')
    def post(self):
        body_array = request.json
        resposta = []

        for body in body_array:
            erro_equipamento = EquipamentoSchema().validate(body)
            if erro_equipamento:
                resposta.append(erro_equipamento)
                continue

            equipamento_existente = equipamento_service.consultar_numero_de_serie(
                body["numero_de_serie"]
            )

            if equipamento_existente:
                resposta.append({
                    "error": True,
                    "message": "Número de série já cadastrado",
                    "numero_de_serie": equipamento_existente["numero_de_serie"],
                    "status": 400
                })
                continue

            novo_equipamento_id = equipamento_service \
                .registar_equipamento(body)
            resposta.append({"_id": novo_equipamento_id, "status": 200})

        return jsonify(resposta)


    @swag_from('../../documentacao/equipamento/equipamento_put_many.yml')
    def put(self):
        body_array = request.json
        resposta = []

        for body in body_array:
            if '_id' not in body:
                resposta.append({"error": True, "message": "Id é campo obrigatório."})
                continue

            _id = body['_id']

            erro_equipamento = EquipamentoSchema().validate(body)
            if erro_equipamento:
                resposta.append(erro_equipamento)
                continue

            equipamento_existente = equipamento_service.consultar_numero_de_serie(
                body["numero_de_serie"]
            )

            if equipamento_existente is None:
                resposta.append({
                    "error": True,
                    "message": "Equipamento não encontrado",
                    "status": 400
                })
                continue

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

            del body["_id"]
            equipamento_service.atualizar_equipamento(body, _id)
            resposta.append({"_id": _id})

        return jsonify(resposta)


    @swag_from('../../documentacao/equipamento/equipamento_patch_many.yml')
    def patch(self):
        pass


    @swag_from('../../documentacao/equipamento/equipamento_delete_many.yml')
    def delete(self):
        body_array = request.args
        resposta = []

        for body in body_array:
            if '_id' not in body:
                resposta.append({"error": True, "message": "Id é campo obrigatório."})
                continue

            _id = body['_id']

            equipamento = equipamento_service.listar_equipamento_by_id(_id)
            if equipamento is None:
                resposta.append({
                    "error": True,
                    "message": "Equipamento não encontrado",
                    "status": 400
                })
                continue

            equipamento_service.deletar_equipamento(_id)

        if resposta:
            return jsonify(resposta)

        return jsonify('', 200)


class EquipamentoOne(Resource):
    @swag_from('../../documentacao/equipamento/equipamento_get_one.yml')
    def get(self, _id):
        equipamento = equipamento_service.listar_equipamento_by_id(_id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrada..."), 404)
        return Response(equipamento.to_json(),
                        mimetype="application/json",
                        status=200)


    @swag_from('../../documentacao/equipamento/equipamento_put_one.yml')
    def put(self, _id):
        equipamento = equipamento_service.listar_equipamento_by_id(_id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrada..."), 400)

        body = request.get_json()
        erro_equipamento = EquipamentoSchema().validate(body)
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


    @swag_from('../../documentacao/equipamento/equipamento_patch_one.yml')
    def patch(self):
        pass


    @swag_from('../../documentacao/equipamento/equipamento_delete_one.yml')
    def delete(self, _id):
        equipamento = equipamento_service.listar_equipamento_by_id(_id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrado..."), 400)
        equipamento_service.deletar_equipamento(_id)
        return make_response('', 204)


class EquipamentoFind(Resource):
    @swag_from('../../documentacao/equipamento/equipamento_find.yml')
    def post(self):
        pass


class EquipamentoBulk(Resource):
    def post(self):
        body = request.json
        if 'equipamentos' not in body:
            return error_response('Equipamentos não enviado')

        a = []
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

    erro_equipamento = EquipamentoSchema().validate(body)
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
