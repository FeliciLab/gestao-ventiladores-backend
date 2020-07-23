from api.v2.models.equipamento_model import Equipamento


class EquipmentBuilder:
    def __init__(self):
        self.equipamento = Equipamento()

    def set_equipamento(self, eqp_data):
        for k, v in eqp_data.items():
            self.equipamento[k] = v

    def get_equipamento(self):
        return self.equipamento
