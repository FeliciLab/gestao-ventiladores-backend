import os
from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename
from ..services import ordem_servico_service
import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
import json


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def build_name(id_ordem_servico_string, photo_category, extensions):
    return id_ordem_servico_string + "_" + photo_category + "." + extensions


def get_extention(file_name):
    return file_name.rsplit('.', 1)[1].lower()


def save_photo(request):
    ordem_servico = ordem_servico_service.registrar_equipamento_vazio()

    final_name_file = None
    file = None

    if 'foto_antes_limpeza' in request.files:

        photo_type = "foto_antes_limpeza"
        file = request.files[photo_type]
        file_name = file.filename
        final_name_file = build_name(str(ordem_servico.id), photo_type,
                                     get_extention(file_name))

        ordem_servico.triagem.foto_antes_limpeza = final_name_file

    elif 'foto_apos_limpeza' in request.files:

        photo_type = "foto_apos_limpeza"

        file = request.files[photo_type]
        file_name = file.filename
        final_name_file = build_name(str(ordem_servico.id), photo_type,
                                     get_extention(file_name))
        ordem_servico.triagem.foto_apos_limpeza = final_name_file

    else:
        return "erro"

    ordem_servico.save()

    # filename = secure_filename(final_name_file)

    file.save(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'storage',
                     secure_filename(final_name_file))
    )

    return str(ordem_servico.id)


def replace_photo(request):
    _id = request.form["_id"]
    ordem_servico = json.loads(ordem_servico_service.listar_ordem_servico_by_id(_id))

    file = None
    final_name_file = None

    if 'foto_antes_limpeza' in request.files:

        photo_type = "foto_antes_limpeza"
        file = request.files[photo_type]

        file_name = file.filename
        final_name_file = build_name(str(_id), photo_type,
                                     get_extention(file_name))

        ordem_servico['triagem']['foto_antes_limpeza'] = final_name_file

    elif 'foto_apos_limpeza' in request.files:

        photo_type = "foto_apos_limpeza"
        file = request.files[photo_type]

        file_name = file.filename
        final_name_file = build_name(str(_id), photo_type,
                                     get_extention(file_name))

        ordem_servico['triagem']['foto_apos_limpeza'] = final_name_file

    del ordem_servico["_id"]
    del ordem_servico["created_at"]
    del ordem_servico["updated_at"]

    ordem_servico_service.atualizar_ordem_servico_by_ordem_servico(ordem_servico, _id)

    file.save(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'storage',
                     secure_filename(final_name_file))
    )

    return _id


class TriagemImagem(Resource):
    # def get(self):
    #     body = request.args
    #     ordem_servico = json.loads(ordem_servico_service.listar_ordem_servico_by_id(body["_id"]))
    #
    #     path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'storage',
    #                         ordem_servico['triagem']['foto_antes_limpeza'])
    #     os.remove(path)
    #     if 'foto_antes_limpeza' in body:
    #         ordem_servico.triagem.foto_antes_limpeza = body['foto_antes_limpeza']
    #     elif 'foto_apos_limpeza' in body:
    #         ordem_servico.triagem.foto_apos_limpeza = body['foto_apos_limpeza']
    #     else:
    #         return 'erro'
    #     ordem_servico_service.atualizar_ordem_servico(ordem_servico, body["_id"])
    #
    #     if 'foto_antes_limpeza' in body:
    #         file = body['foto_antes_limpeza']
    #     elif 'foto_apos_limpeza' in body:
    #         file = body['foto_apos_limpeza']
    #     filename = secure_filename(str(ordem_servico.id) + file.filename)
    #     file.save(
    #         os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'storage', filename)
    #     )
    #     return 'get'

    def post(self):
        # Criar documento
        result = ""

        if "_id" in request.form and not request.form["_id"] is "":
            result = replace_photo(request)

        else:
            result = save_photo(request)

        return result
