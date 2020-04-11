from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..schemas import equipamento_schema
from ..services import equipamento_service
from flasgger import swag_from
# from documentacao.exemplo import teste
from ..utils.importador_de_equipamentos import importar_triagem


class EquipamentoList(Resource):
    #   @swag_from(teste)
    def get(self):  # OK
        equipamentos = equipamento_service.listar_equipamentos()
        return Response(equipamentos, mimetype="application/json", status=200)

    #    @swag_from('../../documentacao/equipamento_post.yml')
    def post(self):  # OK
        body = request.json
        equipamento_cadatrado = equipamento_service.listar_equipamento_id(body['numero_ordem_servico'])
        if equipamento_cadatrado:
            return make_response(jsonify("Equipamento já cadastrado..."), 403)
        es = equipamento_schema.EquipamentoSchema()
        et = equipamento_schema.TriagemSchema()
        ea = equipamento_schema.AcessorioSchema()
        erro_equipamento = es.validate(body)
        erro_triagem = et.validate(body["triagem"])
        if erro_equipamento:
            return make_response(jsonify(erro_equipamento), 400)
        elif erro_triagem:
            return make_response(jsonify(erro_triagem), 400)
        for acessorio in body["triagem"]["acessorios"]:
            if ea.validate(acessorio):
                return make_response(jsonify(ea.validate(acessorio)), 400)
        novo_equipamento = equipamento_service.registrar_equipamento(body)
        return Response(novo_equipamento, mimetype="application/json", status=201)


class EquipamentoDetail(Resource):
    def get(self, numero_ordem_servico):  # OK
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

