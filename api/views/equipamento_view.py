from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..schemas import equipamento_schema
from ..services import equipamento_service
from utils import importador_de_equipamentos

class EquipamentoList(Resource):
    def get(self): # OK
        equipamentos = equipamento_service.listar_equipamentos()
        return Response(equipamentos, mimetype="application/json", status=200)

    def post(self): # OK
        body = request.json
        equipamento_cadatrado = equipamento_service.listar_equipamento_id(body['numero_ordem_servico'])
        if equipamento_cadatrado:
            return make_response(jsonify("Equipamento já cadastrado..."), 403)
        es = equipamento_schema.EquipamentoSchema()
        et = equipamento_schema.TriagemSchema()
        erro_equipamento = es.validate(request.json)
        erro_triagem = et.validate(request.json["triagem"])
        if erro_equipamento:
            return make_response(jsonify(erro_equipamento), 400)
        elif erro_triagem:
            return make_response(jsonify(erro_triagem), 400)
        else:
            novo_equipamento = equipamento_service.registrar_equipamento(body)
            return Response(novo_equipamento, mimetype="application/json", status=201)


class EquipamentoDetail(Resource):
    def get(self, numero_ordem_servico): # OK
        equipamento = equipamento_service.listar_equipamento_id(numero_ordem_servico)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrado..."), 404)
        return Response(equipamento, mimetype="application/json", status=200)

    def put(self, numero_ordem_servico):
        equipamento = equipamento_service.listar_equipamento_id(numero_ordem_servico)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrado..."), 404)
        body = request.get_json()
        if 'clinico' in body:
            erro_clinico = equipamento_schema.ClinicoSchema().validate(body['clinico'])
            if erro_clinico:
                return make_response(jsonify(erro_clinico), 400)
        elif 'tecnico' in body:
            erro_tecnico = equipamento_schema.TecnicoSchema().validate(body['tecnico'])
            if erro_tecnico:
                return make_response(jsonify(erro_tecnico), 400)
            et = equipamento_schema.TriagemSchema().validate(body)
        equipamento_service.atualizar_equipamento(body, numero_ordem_servico)
        equipamento_atualizado = equipamento_service.listar_equipamento_id(numero_ordem_servico)
        return Response(equipamento_atualizado, mimetype="application/json", status=200)

    def delete(self, numero_ordem_servico):
        equipamento = equipamento_service.listar_equipamento_id(numero_ordem_servico)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrado..."), 404)
        equipamento_service.deletar_equipamento(numero_ordem_servico)
        return make_response('', 204)


class EquipamentoImportacao(Resource):
    def post(self):
        body = request.json
        resultado_da_importacao_dt = importador_de_equipamentos.tratar_importacao(body)

        if "erro" in resultado_da_importacao_dt:
            make_response(jsonify(resultado_da_importacao_dt["erro"]), 404)
        else:
            make_response(jsonify(resultado_da_importacao_dt["ok"]), 200)



