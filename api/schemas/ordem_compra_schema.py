from ..models import ordem_compra_model
from marshmallow import Schema, fields


class OrdemCompraSchema(Schema):
    class Meta:
        model = ordem_compra_model.OrdemCompra
        fields = ("numero_ordem_compra", "itens")

    numero_ordem_compra = fields.String(required=False)
    itens = fields.List(fields.String, required=False)


