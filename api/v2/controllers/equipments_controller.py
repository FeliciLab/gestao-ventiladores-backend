from flask_restful import Resource
from ..services.equipments_service import EquipmentsService
from .dtos.equipments_response import EquipmentsResponse


class EquipmentsController(Resource):
    def __init__(self):
        self.service = EquipmentsService()

    def get(self):
        all_equipments = self.service.get_all()
        equipments_response = EquipmentsResponse(all_equipments).get_equipments
        return {'content': equipments_response}, 200
