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


def build_name(id_equipamento_string, photo_category, extention):
    return id_equipamento_string + "_" + photo_category + "." + extention


def get_extention(file_name):
    return file_name.rsplit('.', 1)[1].lower()


def save_photo(request):
    equipamento = equipamento_service.registrar_equipamento_vazio()

    final_name_file = None
    file = None

    if 'foto_antes_limpeza' in request.files:

        photo_type = "foto_antes_limpeza"
        file = request.files[photo_type]
        file_name = file.filename
        final_name_file = build_name(str(equipamento.id), photo_type,
                                     get_extention(file_name))

        equipamento.triagem.foto_antes_limpeza = final_name_file

    elif 'foto_apos_limpeza' in request.files:

        photo_type = "foto_apos_limpeza"

        file = request.files[photo_type]
        file_name = file.filename
        final_name_file = build_name(str(equipamento.id), photo_type,
                                     get_extention(file_name))
        equipamento.triagem.foto_apos_limpeza = final_name_file

    else:
        return "erro"

    equipamento.save()

    # filename = secure_filename(final_name_file)

    file.save(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'storage',
                     secure_filename(final_name_file))
    )

    return str(equipamento.id)


def replace_photo(request):
    _id = request.form["_id"]
    equipamento = json.loads(equipamento_service.listar_equipamento(_id))

    file = None
    final_name_file = None

    if 'foto_antes_limpeza' in request.files:

        photo_type = "foto_antes_limpeza"
        file = request.files[photo_type]

        file_name = file.filename
        final_name_file = build_name(str(_id), photo_type,
                                     get_extention(file_name))

        equipamento['triagem']['foto_antes_limpeza'] = final_name_file

    elif 'foto_apos_limpeza' in request.files:

        photo_type = "foto_apos_limpeza"
        file = request.files[photo_type]

        file_name = file.filename
        final_name_file = build_name(str(_id), photo_type,
                                     get_extention(file_name))

        equipamento['triagem']['foto_apos_limpeza'] = final_name_file

    del equipamento["_id"]
    del equipamento["created_at"]
    del equipamento["updated_at"]

    equipamento_service.atualizar_equipamento_by_id(equipamento, _id)

    file.save(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'storage',
                     secure_filename(final_name_file))
    )

    return _id


class TriagemImagem(Resource):
    def get(self):
        body = request.args
        equipamento = json.loads(equipamento_service.listar_equipamento(body["_id"]))

        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'storage',
                            equipamento['triagem']['foto_antes_limpeza'])
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
        # Criar documento
        result = ""

        if not request.form["_id"] is "":
            result = replace_photo(request)

        else:
            result = save_photo(request)

        return result
