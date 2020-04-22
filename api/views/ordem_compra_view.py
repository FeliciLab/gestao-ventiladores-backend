from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..services import ordem_compra_service
from flasgger import swag_from

class NumeroOrdemServicoList(Resource):
    def get(self):
        """ Retorna todas as ordens de compra """
        ordem_compra_registrada = ordem_compra_service.listar_ordem_compras().to_json()
        return Response(ordem_compra_registrada, mimetype="application/json", status=201)

    @swag_from('../../documentacao/ordem_compra/ordem_compra_post.yml')
    def post(self):
        """
         Cadastra uma nova ordem de compra caso a requisição venha sem "_id"
         Atualiza a ordem de compra caso a requisição venha com "_id"
        """
        body = request.json
        existe_id = body.get('_id')

        if existe_id:
            ordem_compra_service.atualizar_ordem_compra(body['_id'], body)
            nova_ordem_compra = ordem_compra_service.listar_ordem_compra_by_id(body['_id']).to_json()
        else:
            nova_ordem_compra = ordem_compra_service.registar_ordem_compra(body).to_json()
        return Response(nova_ordem_compra, mimetype="application/json", status=201)

class NumeroOrdemServicoDetail(Resource):
    def get(self, _id):
        """ Retorna uma ordem de compra específica conforme o id passado """
        ordem_compra = ordem_compra_service.listar_ordem_compra_by_id(_id).to_json()
        return Response(ordem_compra, mimetype="application/json", status=201)


    def put(self, _id):
        """ Atualiza a ordem de compra """
        body = request.json
        ordem_compra_service.atualizar_ordem_compra(_id, body)
        nova_ordem_compra = ordem_compra_service.listar_ordem_compra_by_id(_id).to_json()
        return Response(nova_ordem_compra, mimetype="application/json", status=201)


    def delete(self, _id):
        """ Remover uma ordem de compra """
        ordem_compra_service.deletar_ordem_compra(_id)
        return jsonify({"ok": True})

class NumeroOrdemServicoFind(Resource):
    def post(self, _id):
        pass