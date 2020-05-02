from flask import Response, request
from flask_restful import Resource
from ..services import log_service


class LogQuery(Resource):
    def post(self):
        body = request.json
        dados_filtrados = log_service.log_queries(body)
        return Response(dados_filtrados, mimetype="application/json", status=200)