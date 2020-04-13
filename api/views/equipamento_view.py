from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..schemas import equipamento_schema
from ..services import equipamento_service
from ..utils.importador_de_equipamentos import importar_triagem
from flasgger import swag_from


class EquipamentoList(Resource):
    @swag_from('../../documentacao/equipamentos_get.yml')
    def get(self):
        equipamentos = equipamento_service.listar_equipamentos()
        return Response(equipamentos, mimetype="application/json", status=200)

    @swag_from('../../documentacao/equipamentos_post.yml')
    def post(self):
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
    @swag_from('../../documentacao/equipamento_get.yml')
    def get(self, numero_ordem_servico):
        equipamento = equipamento_service.listar_equipamento_id(numero_ordem_servico)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrado..."), 404)
        return Response(equipamento, mimetype="application/json", status=200)

    @swag_from('../../documentacao/equipamento_put.yml')
    def put(self, numero_ordem_servico):
        equipamento = equipamento_service.listar_equipamento_id(numero_ordem_servico)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrado..."), 404)
        body = request.get_json()
        if 'diagnostico' in body:
            erro_diagnostico = equipamento_schema.DiagnosticoSchema().validate(body['diagnostico'])
            if erro_diagnostico:
                return make_response(jsonify(erro_diagnostico), 400)
        if 'acessorios_extras' in body['diagnostico']:
            for acessorios_extra in body['diagnostico']['acessorios_extras']:
                erro_acessorio_extra = equipamento_schema.AcessorioExtraSchema().validate(acessorios_extra)
                if erro_acessorio_extra:
                    return make_response(jsonify(erro_acessorio_extra), 400)
        if 'itens' in body['diagnostico']:
            for itens in body['diagnostico']['itens']:
                item = equipamento_schema.ItemSchema().validate(itens)
                if item:
                    return make_response(jsonify(item), 400)
        equipamento_service.atualizar_equipamento(body, numero_ordem_servico)
        equipamento_atualizado = equipamento_service.listar_equipamento_id(numero_ordem_servico)
        return Response(equipamento_atualizado, mimetype="application/json", status=200)

    @swag_from('../../documentacao/equipamento_delete.yml')
    def delete(self, numero_ordem_servico):
        equipamento = equipamento_service.listar_equipamento_id(numero_ordem_servico)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrado..."), 404)
        equipamento_service.deletar_equipamento(numero_ordem_servico)
        return make_response('', 204)

class EquipamentoFind(Resource):
    @swag_from('../../documentacao/equipamento_find.yml')
    def post(self):
        body = request.json
        if "status" not in body:
            return make_response(jsonify("Não existe a chave status no body"), 404)
        equipamentos = equipamento_service.lista_equipamentos_status(body['status'])
        return Response(equipamentos, mimetype="application/json", status=200)
