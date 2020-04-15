import os
from flask import make_response, jsonify, request, Response, url_for, flash
from flask_restful import Resource
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
        print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        args = request.form
        print(args)
        file = request.files['foto_antes_limpeza']

        from werkzeug.utils import secure_filename
        filename = secure_filename(file.filename)

        file.save(
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'storage', filename)
        )

        return url_for('upload_files', filename=filename)
        # print(body)
        # if '_id' in body:
        #     # Atualizar documento
        #     equipamento_service.atualizar_foto_equipamento_id(body,
        #     body["_id"])
        #     equipamento = equipamento_service.listar_equipamento(body["_id"])
        # else:
        #     # Criar documento
        #    equipamento_service.registrar_equipamento_foto(body)
        # return Response(equipamento, mimetype="application/json", status=200)
