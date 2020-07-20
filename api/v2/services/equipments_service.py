from .service_base import ServiceBase
from ..repositories.equipments_repository import EquipmentRepository


class EquipmentsService(ServiceBase):

    def __init__(self):
        self.repository = EquipmentRepository()

    def getAll(self):
        return self.repository.fetch_all()
