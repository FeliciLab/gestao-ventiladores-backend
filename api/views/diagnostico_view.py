from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..schemas import ordem_servico_schema
from ..services import ordem_servico_service, diagnostico_service
from ..services.diagnostico_service import DiagnosticService


class DiagnosticoDetail(Resource):
    def post(self, _id):
        novo_diagnostico_body = request.json
        ordem_servico = ordem_servico_service.listar_ordem_servico_by_id(_id)
        if ordem_servico is None:
            return make_response(jsonify("Ordem de serviço não encontrado..."), 403)

        erro_diagnostico = ordem_servico_schema.DiagnosticoSchema().validate(novo_diagnostico_body["diagnostico"])
        if erro_diagnostico:
            return make_response(jsonify(erro_diagnostico), 400)

        diagnostico_service.registar_diagnostico(_id, novo_diagnostico_body)
        ordem_servico_atualizada = ordem_servico_service.listar_ordem_servico_by_id(_id)
        return Response(ordem_servico_atualizada, mimetype="application/json", status=201)


class DiagnosticoCrud(Resource):
    def get(self):
        ordem_servicos = DiagnosticService().getDiagnostics()
        return Response(ordem_servicos, mimetype="application/json",
                        status=200)