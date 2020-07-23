from .service_base import ServiceBase
from ..repositories.equipments_repository import EquipmentRepository


class EquipmentsService(ServiceBase):

    def __init__(self):
        self.repository = EquipmentRepository()

    def get_all(self):
        return self.repository.fetch_all()
