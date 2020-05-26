from flask import Response, request
from flask_restful import Resource
from ..services import log_service
from flasgger import swag_from

class LogQuery(Resource):
    @swag_from('../../documentacao/log/log_find.yml')
    def post(self):
        body = request.json
        dados_filtrados = log_service.log_queries(body)
        return Response(dados_filtrados,
                        mimetype="application/json",
                        status=200)
