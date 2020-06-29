from flask_restful import Resource
from flask import send_from_directory, abort
from api.v2.helpers.helper_response import error_response


class ServiceOrderImageController(Resource):
    def get(self, id, img=None):
        if img == None:
            img = 'foto_antes_limpeza.jpg'

        return send_from_directory(
            'api/storage/',
            filename=f'{id}_{img}',
            as_attachment=False)
