from ..models import ordem_servico_model
from marshmallow import Schema, fields


class EquipamentoSchema(Schema):
    class Meta:
        model = ordem_servico_model.OrdemServico
        fields = (
            "numero_de_serie", "nome_equipamento", "numero_do_patrimonio", "tipo", "marca", "modelo",
            "fabricante", "municipio_origem", "nome_instituicao_origem", "tipo_instituicao_origem",
            "nome_responsavel", "contato_responsavel", "created_at", "updated_at"
        )

    numero_de_serie = fields.String(required=True)
    nome_equipamento = fields.String(required=True)
    numero_do_patrimonio = fields.String(required=True)
    tipo = fields.String(required=True)
    marca = fields.String(required=True)
    modelo = fields.String(required=True)
    fabricante = fields.String(required=True)
    municipio_origem = fields.String(required=True)
    nome_instituicao_origem = fields.String(required=True)
    tipo_instituicao_origem = fields.String(required=True)
    nome_responsavel = fields.String(required=True)
    contato_responsavel = fields.String(required=True)

    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)