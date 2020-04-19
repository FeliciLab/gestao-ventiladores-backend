import json

from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..schemas import ordem_servico_schema
from ..services import ordem_servico_service, equipamento_service
from flasgger import swag_from


def validacao_ordem_servico(body):
    es = ordem_servico_schema.OrdemServicoSchema()
    erro_ordem_servico = es.validate(body)
    if erro_ordem_servico:
        return make_response(jsonify(erro_ordem_servico), 400)


def validacao_triagem(body):
    et = ordem_servico_schema.TriagemSchema()
    erro_triagem = et.validate(body["triagem"])
    if erro_triagem:
        return make_response(jsonify(erro_triagem), 400)


def validacao_diagnostico(body):
    ed = ordem_servico_schema.DiagnosticoSchema()
    erro_diagnostico = ed.validate(body["diagnostico"])
    if erro_diagnostico:
        return make_response(jsonify(erro_diagnostico), 400)


def validacao_acessorios(body):
    ea = ordem_servico_schema.AcessorioSchema()
    for acessorio in body["triagem"]["acessorios"]:
        erro_acessorio = ea.validate(acessorio)
        if erro_acessorio:
            return make_response(jsonify(erro_acessorio), 400)


def validacao_itens(body):
    ei = ordem_servico_schema.ItemSchema()
    for item in body["diagnostico"]["itens"]:
        erro_item = ei.validate(item)
        if erro_item:
            return make_response(jsonify(erro_item), 400)


class OrdemServicoList(Resource):
    # todo Denis atualizar essa url do swag
    @swag_from('../../documentacao/equipamento/equipamentos_get.yml')
    def get(self):
        """
            Retorna todos as ordens de servico com o equipamento relacionado
        """
        ordem_servico = ordem_servico_service.listar_ordem_servico()
        return Response(ordem_servico.to_json(), mimetype="application/json", status=200)

    """
        Cadastra uma nova ordem de servico - triagem ou
        Cadastra uma nova ordem de servico - triagem e diagnostico
        Adiciona um novo diagnostico ou
    """

    # todo Denis atualizar essa url do swag
    @swag_from('../../documentacao/equipamento/equipamentos_post.yml')
    def post(self):
        body = request.json
        ordem_servico_cadastrado = ordem_servico_service.listar_ordem_servico_by_numero_ordem_servico(
            body['numero_ordem_servico'])

        if 'triagem' in body and 'diagnostico' in body:
            if ordem_servico_cadastrado:
                return make_response(jsonify("Ordem de Serviço já cadastrada..."), 403)

            validacao_ordem_servico(body)
            validacao_triagem(body)
            validacao_diagnostico(body)
            validacao_acessorios(body)
            validacao_itens(body)

            equipamento = equipamento_service.listar_equipamento(body["equipamento_id"])
            body["equipamento_id"] = equipamento
            novo_ordem_servico = ordem_servico_service.registrar_ordem_servico(body)
            return Response(novo_ordem_servico.to_json(), mimetype="application/json", status=201)

        elif 'triagem' in body:
            if ordem_servico_cadastrado:
                return make_response(jsonify("Ordem de Serviço já cadastrada..."), 403)

            validacao_ordem_servico(body)
            validacao_triagem(body)
            validacao_acessorios(body)

            equipamento = equipamento_service.listar_equipamento(body["equipamento_id"])
            body["equipamento_id"] = equipamento
            novo_ordem_servico = ordem_servico_service.registrar_ordem_servico(body)
            return Response(novo_ordem_servico.to_json(), mimetype="application/json", status=201)

        elif 'diagnostico' in body:
            if ordem_servico_cadastrado is None:
                return make_response(jsonify("Ordem de Serviço não cadastrada..."), 403)

            validacao_ordem_servico(body)
            validacao_diagnostico(body)
            validacao_itens(body)

            equipamento = equipamento_service.listar_equipamento(body["equipamento_id"])
            body["equipamento_id"] = equipamento

            ordem_servico_service.atualizar_ordem_servico(str(ordem_servico_cadastrado.id), body)

            novo_ordem_servico = ordem_servico_service.listar_ordem_servico_by_numero_ordem_servico(
            body['numero_ordem_servico'])

            return Response(novo_ordem_servico.to_json(), mimetype="application/json", status=201)

        else:
            return make_response(jsonify('Ordem de servico necessita das chave "triagem" ou "diagnostico"'), 400)


class OrdemServicoDetail(Resource):
    # todo Denis atualizar essa url do swag
    @swag_from('../../documentacao/equipamento/equipamento_get.yml')
    def get(self, _id):
        ordem_servico = ordem_servico_service.listar_ordem_servico_by_id(_id)
        if ordem_servico is None:
            return make_response(jsonify("Ordem de serviço não encontrada..."), 404)
        return Response(ordem_servico.to_json(), mimetype="application/json", status=200)

    # todo Denis atualizar essa url do swag
    @swag_from('../../documentacao/equipamento/equipamento_put.yml')
    def put(self, _id):
        ordem_servico = ordem_servico_service.listar_ordem_servico_by_id(_id)

        if ordem_servico is None:
            return make_response(jsonify("Ordem de serviço não encontrada..."), 404)
        body = request.get_json()
        es = ordem_servico_schema.OrdemServicoSchema()
        et = ordem_servico_schema.TriagemSchema()
        ea = ordem_servico_schema.AcessorioSchema()
        erro_ordem_servico = es.validate(body)
        erro_triagem = et.validate(body["triagem"])
        if erro_ordem_servico:
            return make_response(jsonify(erro_ordem_servico), 400)
        elif erro_triagem:
            return make_response(jsonify(erro_triagem), 400)
        for acessorio in body["triagem"]["acessorios"]:
            erro_acessorio = ea.validate(acessorio)
            if erro_acessorio:
                return make_response(jsonify(erro_acessorio), 400)
            # todo denis, essa mesma validacao que tu vai para itens, tu deve fazer para acessorios

        ordem_servico_service.atualizar_ordem_servico(_id, body)
        ordem_servico_atualizado = ordem_servico_service.listar_ordem_servico_by_id(_id)
        return Response(ordem_servico_atualizado, mimetype="application/json", status=200)

    # todo Denis atualizar essa url do swag
    @swag_from('../../documentacao/equipamento/equipamento_delete.yml')
    def delete(self, _id):
        ordem_servico = ordem_servico_service.listar_ordem_servico_by_id(_id)
        if ordem_servico is None:
            return make_response(jsonify("Ordem de serviço não encontrada..."), 404)

        ordem_servico_service.deletar_ordem_servico(_id)
        return make_response('', 204)


class OrdemServicoFind(Resource):
    # todo Denis atualizar essa url do swag
    @swag_from('../../documentacao/equipamento/equipamento_find.yml')
    def post(self):
        body = request.json
        if "status" not in body:
            return make_response(jsonify("Não existe a chave status no body"), 404)
        ordem_servico_list = ordem_servico_service.listar_ordem_servico_status(body['status'])
        return Response(ordem_servico_list.to_json(), mimetype="application/json", status=200)


class OrdemServicoFiltragem(object):
    def post(self):
        body = request.json
        body_filter = ordem_servico_service.filtering_ordem_servico_queries(body)
        return Response(body_filter, mimetype="application/json", status=200)
