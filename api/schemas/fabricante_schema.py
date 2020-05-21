from ..models import fabricante_model
from marshmallow import Schema, fields


class MarcaSchema(Schema):
    class Meta:
        model = fabricante_model.Fabricante
        fields = ("marca", "modelos")

    marca = fields.String(required=True)
    modelos = fields.List(fields.String, required=True)


class FabricanteSchema(Schema):
    class Meta:
        model = fabricante_model.Fabricante
        fields = ("fabricante_nome", "marcas")

    fabricante_nome = fields.String(required=True)
    marcas = fields.List(fields.Nested(MarcaSchema), required=True)
