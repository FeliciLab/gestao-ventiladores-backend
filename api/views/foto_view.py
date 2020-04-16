import os
from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename
from ..services import equipamento_service
import os
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
import json

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class TriagemImagem(Resource):
    def get(self):
        body = request.args
        equipamento = json.loads(equipamento_service.listar_equipamento(body["_id"]))
        print(equipamento['triagem']['foto_antes_limpeza'])
        print(type(equipamento['triagem']['foto_antes_limpeza']))
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'storage', equipamento['triagem']['foto_antes_limpeza'])
        os.remove(path)
        if 'foto_antes_limpeza' in body:
            equipamento.triagem.foto_antes_limpeza = body['foto_antes_limpeza']
        elif 'foto_apos_limpeza' in body:
            equipamento.triagem.foto_apos_limpeza = body['foto_apos_limpeza']
        else:
            return 'erro'
        equipamento_service.atualizar_equipamento(equipamento, body["_id"])

        if 'foto_antes_limpeza' in body:
            file = body['foto_antes_limpeza']
        elif 'foto_apos_limpeza' in body:
            file = body['foto_apos_limpeza']
        filename = secure_filename(str(equipamento.id) + file.filename)
        file.save(
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'storage', filename)
        )
        return 'get'

    def post(self):
        file = request.files
        print(request.form)
        # Criar documento
        equipamento = equipamento_service.registrar_equipamento_vazio()
        if 'foto_antes_limpeza' in request.files:
            file = request.files['foto_antes_limpeza']
            equipamento.triagem.foto_antes_limpeza = str(equipamento.id) + '_foto_antes_limpeza_' + file.filename.rsplit('.', 1)[1].lower()
        else:
            file = request.files['foto_apos_limpeza']
            equipamento.triagem.foto_apos_limpeza = str(equipamento.id) + '_foto_apos_limpeza_' + file.filename.rsplit('.', 1)[1].lower()
        equipamento.save()
        filename = secure_filename(str(equipamento.id) + file.filename)
        file.save(
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'storage', filename)
        )
        return 'post'