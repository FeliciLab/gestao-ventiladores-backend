from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..schemas import equipamento_schema
from ..services import ordem_servico_service
from flasgger import swag_from


class EquipamentoList(Resource):
    @swag_from('../../documentacao/equipamento/equipamentos_get.yml')
    def get(self):
        equipamentos = ordem_servico_service.listar_equipamentos()
        return Response(equipamentos, mimetype="application/json", status=200)

    @swag_from('../../documentacao/equipamento/equipamentos_post.yml')
    def post(self):
        body = request.json
        equipamento_cadatrado = ordem_servico_service.listar_equipamento_id(body['numero_ordem_servico'])
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
        novo_equipamento = ordem_servico_service.registrar_equipamento(body)
        return Response(novo_equipamento, mimetype="application/json", status=201)


class EquipamentoDetail(Resource):
    @swag_from('../../documentacao/equipamento/equipamento_get.yml')
    def get(self, numero_ordem_servico):
        equipamento = ordem_servico_service.listar_equipamento_id(numero_ordem_servico)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrado..."), 404)
        return Response(equipamento, mimetype="application/json", status=200)

    @swag_from('../../documentacao/equipamento/equipamento_put.yml')
    def put(self, numero_ordem_servico):
        id = numero_ordem_servico
        equipamento = ordem_servico_service.listar_equipamento(id)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrado..."), 404)
        body = request.get_json()
        if 'diagnostico' in body:
            erro_diagnostico = equipamento_schema.DiagnosticoSchema().validate(body['diagnostico'])
            if erro_diagnostico:
                return make_response(jsonify(erro_diagnostico), 400)
            if 'itens' in body['diagnostico']:
                for itens in body['diagnostico']['itens']:
                    item = equipamento_schema.ItemSchema().validate(itens)
                    if item:
                        return make_response(jsonify(item), 400)
        ordem_servico_service.atualizar_equipamento_by_id(body, id)
        equipamento_atualizado = ordem_servico_service.listar_equipamento(id)
        return Response(equipamento_atualizado, mimetype="application/json", status=200)

    @swag_from('../../documentacao/equipamento/equipamento_delete.yml')
    def delete(self, numero_ordem_servico):
        equipamento = ordem_servico_service.listar_equipamento_id(numero_ordem_servico)
        if equipamento is None:
            return make_response(jsonify("Equipamento não encontrado..."), 404)
        ordem_servico_service.deletar_equipamento(numero_ordem_servico)
        return make_response('', 204)


class EquipamentoFind(Resource):
    @swag_from('../../documentacao/equipamento/equipamento_find.yml')
    def post(self):
        body = request.json
        if "status" not in body:
            return make_response(jsonify("Não existe a chave status no body"), 404)
        equipamentos = ordem_servico_service.lista_equipamentos_status(body['status'])
        return Response(equipamentos, mimetype="application/json", status=200)


class EquipamentoFiltragem(object):

    def post(self):
        body = request.json
        body_filter = ordem_servico_service.filtering__equipamento_queries(body)
        return Response(body_filter, mimetype="application/json", status=200)