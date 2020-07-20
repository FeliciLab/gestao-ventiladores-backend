from ..models.equipamento_model import Equipamento


class EquipmentRepository:

    @staticmethod
    def fetch_all(include_deleted=None):
        if include_deleted:
            return Equipamento.objects()
        return Equipamento.objects(deleted_at__exists=False)
