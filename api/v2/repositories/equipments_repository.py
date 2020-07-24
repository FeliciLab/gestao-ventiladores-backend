from ..models.equipamento_model import Equipamento


class EquipmentRepository:

    @staticmethod
    def fetch_all():
       return Equipamento.objects()

    @staticmethod
    def fetch_all_without_deleted():
        return Equipamento.objects(deleted_at__exists=False)
