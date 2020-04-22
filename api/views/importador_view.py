from flask import request, make_response, jsonify
from flask_restful import Resource
from api.utils import importador
from flasgger import swag_from

class TriagemImportacao(Resource):
    # tudo Denis atualizar swag
    #@swag_from('../../documentacao/importacao/importacao_triagem.yml')
    def post(self):
        body = request.json
        resultado_da_importacao_dt = importador.importar_triagem(body)
        print(resultado_da_importacao_dt)
        if "ok" in resultado_da_importacao_dt.keys():
            return make_response(jsonify("Importacao com sucesso..."), 200)
        elif "validate" in resultado_da_importacao_dt:
            return make_response(jsonify(resultado_da_importacao_dt["validate"]), 400)
        else:
            return make_response(jsonify("Erro na importacao..."), 400)


class DiagnosticoImportacao(Resource):
    #@swag_from('../../documentacao/importacao/importacao_diagnostico.yml')
    def post(self):
        body = request.json
        resultado_da_importacao_dt = importador.importar_diagnostino(body)

        if "ok" in resultado_da_importacao_dt:
            return make_response(jsonify("Importacao sucesso..."), 200)
        elif "validate" in resultado_da_importacao_dt:
            return make_response(jsonify(resultado_da_importacao_dt["validate"]), 400)
        else:
            return make_response(jsonify("Erro na importacao..."), 400)
