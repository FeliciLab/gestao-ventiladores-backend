from ..models import equipamento_model
from marshmallow import Schema, fields


class EquipamentoSchema(Schema):
    class Meta:
        model = equipamento_model.Equipamento
        fields = ("numero_ordem_servico", "triagem", "clinico", "tecnico")

    numero_ordem_servico = fields.String(required=True)
    triagem = fields.Dict(required=True)
    clinico = fields.Dict(required=False)
    tecnico = fields.Dict(required=False)