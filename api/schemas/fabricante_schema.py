from ..models import fabricante_model
from marshmallow import Schema, fields


class FabricanteSchema(Schema):
    class Meta:
        model = fabricante_model.Fabricante
        #fields = ("fabricante_nome", "marcas", "modelos")
        fields = ("fabricante_nome", "marcas", "modelos")

    fabricante_nome = fields.String(required=True)
    marcas = fields.List(fields.Dict, required=True)
    #modelos = fields.List(fields.String, required=True)