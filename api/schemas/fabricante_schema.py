from ..models import fabricante_model
from marshmallow import Schema, fields


class FabricanteSchema(Schema):
    class Meta:
        model = fabricante_model.Fabricante
        fields = ("fabricante_nome", "modelo")

    fabricante_nome = fields.String(required=True)
    modelo = fields.List(fields.String, required=True)