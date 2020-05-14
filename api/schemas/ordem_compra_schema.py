from ..models import ordem_compra_model
from marshmallow import Schema, fields


class ItemSchema(Schema):
    tipo = fields.String(required=False)
    nome = fields.String(required=False)
    descricao = fields.String(required=False)
    unidade = fields.String(required=False)
    quantidade = fields.Integer(required=False)
    fabricante = fields.String(required=False)
    codigo = fields.String(required=False)


class OrdemCompraSchema(Schema):
    class Meta:
        model = ordem_compra_model.OrdemCompra
        fields = ("numero_ordem_compra", "itens")

    numero_ordem_compra = fields.String(required=False)
    itens = fields.List(fields.Nested(ItemSchema), required=False)


