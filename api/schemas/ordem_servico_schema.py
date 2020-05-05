from ..models import ordem_servico_model
from marshmallow import Schema, fields, validate


class AcessorioSchema(Schema):
    class Meta:
        model = ordem_servico_model.Acessorio
        fields = ("descricao", "acompanha", "quantidade", "estado_de_conservacao")

    descricao = fields.String(required=False)
    acompanha = fields.Boolean(required=False)
    quantidade = fields.Integer(required=False)
    estado_de_conservacao = fields.String(required=False)


class TriagemSchema(Schema):
    class Meta:
        model = ordem_servico_model.Triagem
        fields = ("nome_equipamento", "foto_antes_limpeza", "tipo", "numero_do_patrimonio",
                  "numero_de_serie", "nome_responsavel", "contato_responsavel",
                  "estado_de_conservacao", "fabricante", "marca", "modelo", "acessorios",
                  "foto_apos_limpeza", "nome_instituicao_origem", "tipo_instituicao_origem",
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
    acessorios = fields.List(fields.Nested(AcessorioSchema), required=True)
    foto_apos_limpeza = fields.String(required=False)
    nome_instituicao_origem = fields.String(required=False)
    tipo_instituicao_origem = fields.String(required=False)
    municipio_origem = fields.String(required=False)

class ItemSchema(Schema):
    class Meta:
        model = ordem_servico_model.Item
        fields = ("nome", "tipo", "quantidade", "descricao", "valor", "prioridade", "unidade_medida")

    nome = fields.String(required=False)
    tipo = fields.String(required=False)
    quantidade = fields.Integer(required=False)
    descricao = fields.String(required=False)
    valor = fields.Float(required=False)
    prioridade = fields.String(required=False)
    unidade_medida = fields.String(required=False)

class DiagnosticoSchema(Schema):
    class Meta:
        model = ordem_servico_model.Triagem
        fields = ("resultado_tecnico", "demanda_servicos", "demanda_insumos", "acao_orientacao", "observacoes",
                  "itens", "acessorios")

    resultado_tecnico = fields.String(required=False)
    demanda_servicos = fields.String(required=False)
    demanda_insumos = fields.String(required=False)
    acao_orientacao = fields.String(required=False)
    observacoes = fields.String(required=False)
    itens = fields.List(fields.Nested(ItemSchema), required=False)

class OrdemServicoSchema(Schema):
    class Meta:
        model = ordem_servico_model.OrdemServico
        fields = (
            "_id", "equipamento_id", "numero_ordem_servico", "created_at", "updated_at", "triagem", "clinico", "tecnico",
            "foto_equipamento_chegada", "status", "diagnostico")

    numero_ordem_servico = fields.String(required=False)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)
    triagem = fields.Nested(TriagemSchema, required=False)
    diagnostico = fields.Nested(DiagnosticoSchema, required=False)
    status = fields.String(validate=validate.OneOf(["triagem", "diagnostico"]), required=False)
