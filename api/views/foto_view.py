from flask import make_response, jsonify, request, Response
from flask_restful import Resource
from ..schemas import equipamento_schema
from ..services import equipamento_service
from flasgger import swag_from
from ..models import equipamento_model
from datetime import datetime

class TriagemImagem(Resource):
    def post(self):
        body = request.json
        if '_id' in body:
            # Atualizar documento
            equipamento_service.atualizar_foto_equipamento_id(body, body["_id"])
            equipamento = equipamento_service.listar_equipamento(body["_id"])
        else:
            # Criar documento
           equipamento_service.registrar_equipamento_foto(body)
        return Response(equipamento, mimetype="application/json", status=200)