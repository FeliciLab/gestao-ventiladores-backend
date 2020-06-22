from marshmallow import Schema, fields, ValidationError
from ...models.item_model import Item


class ItemSchema(Schema):
    class Meta:
        model = Item
        fields = ("_id",
                  "tipo",
                  "fabricante",
                  "codigo",
                  "nome",
                  "unidade_medida",
                  "quantidade",
                  "descricao",
                  "reference_key",
                  "created_at",
                  "updated_at",
                  "deleted_at")

    _id = fields.String(required=False)
    tipo = fields.String(required=False)
    fabricante = fields.String(required=False)
    codigo = fields.String(required=False)
    nome = fields.String(required=True)
    unidade_medida = fields.String(required=True)
    quantidade = fields.Integer(required=True)
    descricao = fields.String(required=False)
    reference_key = fields.String(required=False)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)
    deleted_at = fields.DateTime(required=False)

    def validate_updates(self, item, index):
        try:
            self.load(item, partial=('nome', 'unidade_medida', 'quantidade'))
        except ValidationError as err:
            return {index: err.messages}
