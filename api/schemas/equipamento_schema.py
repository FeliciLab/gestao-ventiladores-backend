from ..models import equipamento_model
from marshmallow import Schema, fields


class EquipamentoSchema(Schema):
    class Meta:
        model = equipamento_model.Equipamento
        fields = (
            "status",
            "numero_de_serie",
            "nome_equipamento",
            "numero_do_patrimonio",
            "tipo",
            "marca",
            "modelo",
            "fabricante",
            "municipio_origem",
            "nome_instituicao_origem",
            "tipo_instituicao_origem",
            "nome_responsavel",
            "contato_responsavel",
            "created_at",
            "updated_at"
        )

    numero_de_serie = fields.String(required=False)
    nome_equipamento = fields.String(required=False)
    numero_do_patrimonio = fields.String(required=False)
    status = fields.String(required=False)
    tipo = fields.String(required=False)
    marca = fields.String(required=False)
    modelo = fields.String(required=False)
    fabricante = fields.String(required=False)
    municipio_origem = fields.String(required=False)
    nome_instituicao_origem = fields.String(required=False)
    tipo_instituicao_origem = fields.String(required=False)
    nome_responsavel = fields.String(required=False)
    contato_responsavel = fields.String(required=False)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)
