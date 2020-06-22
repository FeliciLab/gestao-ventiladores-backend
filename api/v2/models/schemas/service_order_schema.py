from api.v2.models import service_order_model
from .schema_base import SchemaBase
from marshmallow import Schema, fields, validate


class AccessorySchema(Schema):
    class Meta:
        model = service_order_model.Acessorio
        fields = ("descricao",
                  "acompanha",
                  "quantidade",
                  "estado_de_conservacao")

    descricao = fields.String(required=False)
    acompanha = fields.Boolean(required=False)
    quantidade = fields.Integer(required=False)
    estado_de_conservacao = fields.String(required=False)


class ScreeningSchema(Schema):
    class Meta:
        model = service_order_model.Triagem
        fields = ("nome_equipamento",
                  "foto_antes_limpeza",
                  "tipo",
                  "numero_do_patrimonio",
                  "numero_de_serie",
                  "nome_responsavel",
                  "contato_responsavel",
                  "estado_de_conservacao",
                  "fabricante",
                  "marca",
                  "modelo",
                  "acessorios",
                  "foto_apos_limpeza",
                  "nome_instituicao_origem",
                  "tipo_instituicao_origem",
                  "municipio_origem")

    nome_equipamento = fields.String(required=False)
    foto_antes_limpeza = fields.String(required=False)
    tipo = fields.String(required=False)
    numero_do_patrimonio = fields.String(required=False)
    numero_de_serie = fields.String(required=False)
    nome_responsavel = fields.String(required=False)
    contato_responsavel = fields.String(required=False)
    estado_de_conservacao = fields.String(required=False)
    fabricante = fields.String(required=False)
    marca = fields.String(required=False)
    modelo = fields.String(required=False)
    acessorios = fields.List(fields.Nested(AccessorySchema), required=False)
    foto_apos_limpeza = fields.String(required=False)
    nome_instituicao_origem = fields.String(required=False)
    tipo_instituicao_origem = fields.String(required=False)
    municipio_origem = fields.String(required=False)


class ItemSchema(Schema):
    class Meta:
        model = service_order_model.Item
        fields = ("tipo",
                  "fabricante",
                  "codigo",
                  "nome",
                  "unidade_medida",
                  "quantidade",
                  "descricao")

    tipo = fields.String(required=False)
    fabricante = fields.String(required=False)
    codigo = fields.String(required=False)
    nome = fields.String(required=False)
    unidade_medida = fields.String(required=False)
    quantidade = fields.Integer(required=False)
    descricao = fields.String(required=False)


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
    itens = fields.List(fields.Nested(ItemSchema), required=False)


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
                  "diagnostico")

    equipamento_id = fields.String(required=False)
    numero_ordem_servico = fields.String(required=False)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)
    triagem = fields.Nested(ScreeningSchema, required=False)
    diagnostico = fields.Nested(DiagnosticSchema, required=False)
    calibragem = fields.Nested(CalibrationSchema, required=False)
    status = fields.String(validate=validate.OneOf(["triagem", "diagnostico"]),
                           required=False)
