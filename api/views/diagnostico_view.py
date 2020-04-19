from flask import Response, request, make_response, jsonify
from flask_restful import Resource

from ..services import ordem_servico_service, diagnostico_service


class DiagnosticoDetail(Resource):

    def post(self, _id):
        novo_diagnostico_body = request.json
        # todo Denis fazer a validacao de campos do diagnostico
        ordem_servico = ordem_servico_service.listar_ordem_servico_by_id(_id)

        if ordem_servico is None:
            return make_response(jsonify("Ordem de serviço não encontrado..."), 403)

        diagnostico_service.registar_diagnostico(_id, novo_diagnostico_body)

        ordem_servico_atualizada = ordem_servico_service.listar_ordem_servico_by_id(_id)

        return Response(ordem_servico_atualizada.to_json(), mimetype="application/json", status=201)
