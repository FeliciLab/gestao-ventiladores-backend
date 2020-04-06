from flask import request
from api.models.usuario_model import Usuario
from flask_restful import Resource


class UsuarioList(Resource):
    def post(self):
        body = request.get_json()
        usuario = Usuario(**body)
        usuario.gera_hash()
        usuario.save()
        return {'id': str(usuario.id)}, 201
