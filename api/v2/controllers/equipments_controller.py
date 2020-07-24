from flask_restful import Resource
from flask import request
from ..services.equipments_service import EquipmentsService
from .dtos.equipments_response import EquipmentsResponse


class EquipmentsController(Resource):
    def __init__(self):
        self.service = EquipmentsService()

    def get(self):
        include_deleted = False
        body = request.args
        if 'deleted' in body:
            include_deleted = True
        all_equipments = self.service.get_all(include_deleted=include_deleted)
        equipments_response = EquipmentsResponse(all_equipments).get_equipments
        return {'content': equipments_response}, 200
