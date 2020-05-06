import json
from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..schemas import ordem_servico_schema
from ..services import ordem_servico_service, equipamento_service, movimentacao_service, log_service
from ..utils.error_response import error_response
from flasgger import swag_from


class OrdemServicoList(Resource):
    @swag_from('../../documentacao/ordem_servico/ordem_servicos_get.yml')
    def get(self):
        """
            Retorna todos as ordens de servico com o equipamento relacionado
        """
        ordem_servico = ordem_servico_service.listar_ordem_servico()
        return Response(ordem_servico, mimetype="application/json", status=200)

    # todo Denis atualizar essa url do swag
    # @swag_from('../../documentacao/ordem_servico/ordem_servico_post.yml')
    def post(self):
        """
            Cadastra uma nova ordem de servico - triagem ou
            Cadastra uma nova ordem de servico - triagem e diagnostico ou
            Adiciona um novo diagnostico
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

        if 'triagem' in body or 'diagnostico' in body:
            erro_validacao = ordem_servico_schema.OrdemServicoSchema().validate(body)
        else:
            return error_response('Ordem de servico necessita das chave "triagem" ou "diagnostico"')

        if erro_validacao:
            return jsonify(erro_validacao)

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

        log_service.log_atualizacao_ordem_servico('ordem_servico', _id, body)
        ordem_servico_service.atualizar_ordem_servico(_id, body)
        return Response(
            json.dumps({"_id": _id}),
            mimetype="application/json",
            status=200
        )


class OrdemServicoDetail(Resource):
    @swag_from('../../documentacao/ordem_servico/ordem_servico_get.yml')
    def get(self, _id):
        """
            Retorna uma ordem de serviço específica conforme o id do documento repassado.
        """
        ordem_servico = ordem_servico_service.listar_ordem_servico_by_id(_id)
        if ordem_servico is None:
            return make_response(jsonify("Ordem de serviço não encontrada..."), 404)
        return Response(ordem_servico.to_json(), mimetype="application/json", status=200)

    # @swag_from('../../documentacao/ordem_servico/ordem_servico_put.yml')
    def put(self, _id):
        ordem_servico = ordem_servico_service.listar_ordem_servico_by_id(_id)

        if ordem_servico is None:
            return make_response(jsonify("Ordem de serviço não encontrada..."), 404)
        body = request.get_json()

        if 'triagem' in body or 'diagnostico' in body:
            erro_validacao = ordem_servico_schema.OrdemServicoSchema().validate(body)
        else:
            return error_response('Ordem de servico necessita das chave "triagem" ou "diagnostico"')

        if erro_validacao:
            return jsonify(erro_validacao)

        try:
            equipamento_id = body["equipamento_id"]
        except:
            return error_response("ID do equipamento inválido ou não enviado")

        try:
            equipamento = equipamento_service.listar_equipamento_by_id(equipamento_id)
        except:
            return error_response("ID do equipamento inválido")

        if not equipamento:
            return error_response("Equipamento não encontrado")

        body["equipamento_id"] = equipamento

        log_service.log_atualizacao_ordem_servico('ordem_servico', _id, body)
        ordem_servico_service.atualizar_ordem_servico(_id, body)

        return Response(
            json.dumps({"_id": _id}),
            mimetype="application/json",
            status=200
        )

    @swag_from('../../documentacao/ordem_servico/ordem_servico_delete.yml')
    def delete(self, _id):
        """
             Deleta uma ordem de serviço específica conforme o id do documento repassado.
        """
        ordem_servico = ordem_servico_service.listar_ordem_servico_by_id(_id)
        if ordem_servico is None:
            return make_response(jsonify("Ordem de serviço não encontrada..."), 404)

        ordem_servico_service.deletar_ordem_servico(_id)
        return make_response('', 204)


class OrdemServicoQuery(Resource):
    def post(self):
        body = request.json
        dados_filtrados = ordem_servico_service.ordem_servico_queries(body)
        return Response(dados_filtrados, mimetype="application/json", status=200)
