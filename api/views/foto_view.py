import os
from flask import make_response, jsonify, request, Response, url_for, flash
from flask_restful import Resource
from werkzeug.utils import secure_filename
from ..models import equipamento_model
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class TriagemImagem(Resource):
    def get(self):
        body = request.args
        print(body)
        return 'get'

    def post(self):
        if 'foto_antes_limpeza' in request.files:
            file = request.files['foto_antes_limpeza']
        else:
            file = request.files['foto_apos_limpeza']
        print(file)
        # equipamento = Equipamento(foto_antes_limpeza=file['foto_apos_limpeza'])
        equipamento = equipamento_model.Equipamento()
        triagem = equipamento_model.Triagem()
        equipamento.triagem = triagem
        equipamento.save()

        print(f'HEAR: {equipamento.id}')
        filename = secure_filename(str(equipamento.id) + file.filename)
        file.save(
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'storage', filename)
        )

        if 'foto_antes_limpeza' in request.files:
            equipamento.triagem.foto_antes_limpeza = filename
        else:
            equipamento.triagem.foto_apos_limpeza = filename
        equipamento.save()
        #return Response(equipamento, mimetype="application/json", status=201)
        return 'post'

        # Criar um documento vazio - OK
        # Inserir o id do documento no nome da foto - OK
        # Salvar a foto no documento - OK
        # Retornar o id da foto - OK

        # Criar um número de OS temporário e aleatório?
        # Problema: Dois equipamentos sendo registrados no momento da triagem, a OS é unique
