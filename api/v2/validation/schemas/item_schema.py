from marshmallow import Schema, fields
from ...models.item_model import Item

class ItemSchema(Schema):
    class Meta:
        model = Item
        fields = ("tipo",
                  "fabricante",
                  "codigo",
                  "nome",
                  "unidade_medida",
                  "quantidade",
                  "descricao", 
                  "created_at",
                  "updated_at",
                  "deleted_at")

    tipo = fields.String(required=False)
    fabricante = fields.String(required=False)
    codigo = fields.String(required=False)
    nome = fields.String(required=True)
    unidade_medida = fields.String(required=True)
    quantidade = fields.Integer(required=True)
    descricao = fields.String(required=False)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)
    deleted_at = fields.DateTime(required=False)
