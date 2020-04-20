from ..models import ordem_compra
from marshmallow import Schema, fields

class ItemSchema(Schema):
    class Meta:
        model = ordem_compra.Item
        fields = (
            "tipo", "nome_item", "descricao_item", "unidade",
            "quantidade", "fabricante", "codigo_item"
        )

    tipo = fields.String(required=False)
    nome_item = fields.String(required=False)
    descricao_item = fields.String(required=False)
    unidade = fields.String(required=False)
    quantidade = fields.Integer(required=False)
    fabricante = fields.String(required=False)
    codigo_item = fields.String(required=False)


class OrdemCompraSchema(Schema):
    class Meta:
        model = ordem_compra.OrdemCompra
        fields = ("numero_ordem_compra", "itens")

    numero_ordem_compra = fields.String(required=False)
    itens = fields.List(fields.String, required=False)


