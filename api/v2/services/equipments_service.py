from .service_base import ServiceBase
from ..repositories.equipments_repository import EquipmentRepository


class EquipmentsService(ServiceBase):

    def __init__(self):
        self.repository = EquipmentRepository()

    def get_all(self, include_deleted=False):
        if include_deleted:
            return self.repository.fetch_all()
        return self.repository.fetch_all_without_deleted()
