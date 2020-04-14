from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from api.utils import importador_de_equipamentos
from flasgger import swag_from

class TriagemImportacao(Resource):
    @swag_from('../../documentacao/importacao/importacao_triagem.yml')
    def post(self):
        body = request.json
        resultado_da_importacao_dt = importador_de_equipamentos.importar_triagem(body)

        if "ok" in resultado_da_importacao_dt.keys():
            return Response(resultado_da_importacao_dt["ok"], mimetype="application/json", status=200)
        else:
            make_response(jsonify(), 404)
            return make_response(jsonify(resultado_da_importacao_dt["erro"]), 400)


class DiagnosticoClinicoETecnicoImportacao(Resource):
    @swag_from('../../documentacao/importacao/importacao_diagnostico.yml')
    def post(self):
        body = request.json
        resultado_da_importacao_dt = importador_de_equipamentos.importar_diagnostino(body)

        if "ok" in resultado_da_importacao_dt:
            return make_response(jsonify("Importacao sucesso..."), 404)
        else:
            make_response(jsonify(), 404)
            return make_response(jsonify("Fracasso importacao..."), 404)
