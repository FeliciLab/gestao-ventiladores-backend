from api.v2.models import service_order_model
from .schema_base import SchemaBase
from marshmallow import Schema, fields, validate


class AccessorySchema(Schema):
    class Meta:
        model = service_order_model.Acessorio
        fields = ("item_id",
                  "acompanha",
                  "quantidade",
                  "estado_de_conservacao")

    item_id = fields.String(required=True)
    acompanha = fields.Boolean(required=True)
    quantidade = fields.Integer(required=True)
    estado_de_conservacao = fields.String(required=False)


class ScreeningSchema(Schema):
    class Meta:
        model = service_order_model.Triagem
        fields = ("estado_de_conservacao",
                  "foto_antes_limpeza",
                  "acessorios",
                  "foto_apos_limpeza")

    foto_antes_limpeza = fields.String(required=False) 
    estado_de_conservacao = fields.String(required=False)
    acessorios = fields.List(fields.Nested(AccessorySchema), required=False)
    foto_apos_limpeza = fields.String(required=False)


class ItemDiganotico(Schema):
    class Meta:
        model = service_order_model.Item
        fields = ("item_id",
                  "quantidade")

    item_id = fields.String(required=True)
    quantidade = fields.Integer(required=True)


class DiagnosticSchema(Schema):
    class Meta:
        model = service_order_model.Triagem
        fields = ("resultado_tecnico",
                  "demanda_servicos",
                  "observacoes",
                  "itens")

    resultado_tecnico = fields.String(required=False)
    demanda_servicos = fields.String(required=False)
    observacoes = fields.String(required=False)
    itens = fields.List(fields.Nested(ItemDiganotico), required=False)


class CalibrationSchema(Schema):
    class Meta:
        model = service_order_model.Calibragem
        fields = (
            "status",
        )

    status = fields.String(required=False)


class ServiceOrderSchema(Schema, SchemaBase):
    class Meta:
        model = service_order_model.OrdemServico
        fields = ("_id",
                  "equipamento_id",
                  "numero_ordem_servico",
                  "created_at",
                  "updated_at",
                  "triagem",
                  "clinico",
                  "tecnico",
                  "foto_equipamento_chegada",
                  "status",
                  "diagnostico", 
                  "calibragem")

    equipamento_id = fields.String(required=False)
    numero_ordem_servico = fields.Integer(required=True)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)
    triagem = fields.Nested(ScreeningSchema, required=False)
    diagnostico = fields.Nested(DiagnosticSchema, required=False)
    calibragem = fields.Nested(CalibrationSchema, required=True)
    status = fields.String(validate=validate.OneOf(["triagem", "diagnostico"]),
                           required=True)
