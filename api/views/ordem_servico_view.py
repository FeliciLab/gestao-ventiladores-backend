import json
from flasgger import swag_from
from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..schemas import ordem_servico_schema
from ..services import ordem_servico_service, equipamento_service
from ..utils.error_response import error_response


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
    #@swag_from('../../documentacao/ordem_servico/ordem_compra_post.yml')
    def get(self):
        """
            Retorna todos as ordens de servico com o equipamento relacionado
        """
        ordem_servico = ordem_servico_service.listar_ordem_servico()
        return Response(ordem_servico, mimetype="application/json", status=200)

    # todo Denis atualizar essa url do swag
    ##@swag_from('../../documentacao/ordem_servico/ordem_servico_post.yml')
    def post(self):
        """
            Cadastra uma nova ordem de servico - triagem ou
            Cadastra uma nova ordem de servico - triagem e diagnostico
            Adiciona um novo diagnostico ou
        """
        body = request.json
        try:
            _id = body["_id"]
        except:
            _id = False

        try:
            ordem_servico = body["numero_ordem_servico"]
        except:
            return error_response("Ordem de serviço inválido ou inexistente")

        try:
            equipamento_id = body["equipamento_id"]
        except:
            return error_response("ID do equipamento inválido ou não enviado")


        ordem_servico_cadastrado = \
            ordem_servico_service \
                .listar_ordem_servico_by_numero_ordem_servico(ordem_servico)
        if not _id and ordem_servico_cadastrado:
            return error_response("Ordem de Serviço já cadastrada.")

        if 'triagem' in body and 'diagnostico' in body:
            validacao_ordem_servico(body)
            validacao_triagem(body)
            validacao_diagnostico(body)
            validacao_acessorios(body)
            validacao_itens(body)
        elif 'triagem' in body:
            validacao_ordem_servico(body)
            validacao_triagem(body)
            validacao_acessorios(body)
        elif 'diagnostico' in body:
            validacao_ordem_servico(body)
            validacao_diagnostico(body)
            validacao_itens(body)
        else:
            return error_response('Ordem de servico necessita das chave "triagem" ou "diagnostico"')


        try:
            equipamento = equipamento_service.listar_equipamento_by_id(equipamento_id)
        except:
            return error_response("ID do equipamento inválido")

        if not equipamento:
            return error_response("Equipamento não encontrado")

        body["equipamento_id"] = equipamento

        try:
            del body["_id"]
        except KeyError:
            print("_id não está presente no body")

        if not _id:
            novo_ordem_servico = ordem_servico_service.registrar_ordem_servico(body)
            return Response(
                json.dumps({"_id": str(novo_ordem_servico.id)}),
                mimetype="application/json",
                status=201
            )

        ordem_servico_service.atualizar_ordem_servico(_id, body)
        return Response(
            json.dumps({"_id": _id}),
            mimetype="application/json",
            status=200
        )


class OrdemServicoDetail(Resource):
    ##@swag_from('../../documentacao/ordem_servico/ordem_servico_get.yml')
    def get(self, _id):
        """
            Retorna uma ordem de serviço específica conforme o id do documento repassado.
        """
        ordem_servico = ordem_servico_service.listar_ordem_servico_by_id(_id)
        if ordem_servico is None:
            return make_response(jsonify("Ordem de serviço não encontrada..."), 404)
        return Response(ordem_servico.to_json(), mimetype="application/json", status=200)


    ##@swag_from('../../documentacao/ordem_servico/ordem_servico_delete.yml')
    def delete(self, _id):
        """
             Deleta uma ordem de serviço específica conforme o id do documento repassado.
        """
        ordem_servico = ordem_servico_service.listar_ordem_servico_by_id(_id)
        if ordem_servico is None:
            return make_response(jsonify("Ordem de serviço não encontrada..."), 404)

        ordem_servico_service.deletar_ordem_servico(_id)
        return make_response('', 204)


class OrdemServicoFind(Resource):
    #@swag_from('../../documentacao/ordem_servico/ordem_servico_find.yml')
    def post(self):
        """
             Retorna todas as ordens de servico conforme o status que ela possui.
        """
        body = request.json
        if "status" not in body:
            return make_response(jsonify("Não existe a chave status no body"), 404)

        ordem_servico_list = ordem_servico_service.listar_ordem_servico_status(body['status'])
        return Response(ordem_servico_list.to_json(), mimetype="application/json", status=200)


# TODO Lucas essa classe não está sendo utilizada, verificar se ela deve existir.
class OrdemServicoQuery(Resource):
    def post(self):
        body = request.json
        dados_filtrados = ordem_servico_service.ordem_servico_queries(body)
        return Response(dados_filtrados, mimetype="application/json", status=200)
