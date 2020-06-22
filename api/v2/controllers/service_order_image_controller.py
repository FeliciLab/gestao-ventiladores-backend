from flask_restful import Resource
from flask import send_from_directory, abort
from api.v2.helpers.helper_response import error_response


class ServiceOrderImageController(Resource):
    def get(self, id):
        return send_from_directory(
            'api/storage/',
            filename=f'{id}_foto_antes_limpeza.jpg',
            as_attachment=False)
