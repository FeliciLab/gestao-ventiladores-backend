from ..models import equipamento_model
from marshmallow import Schema, fields
from datetime import datetime


class EquipamentoSchema(Schema):
    class Meta:
        model = equipamento_model.Equipamento
        fields = (
            "numero_ordem_servico", "created_at", "updated_at", "triagem", "clinico", "tecnico",
            "foto_equipamento_chegada",
            "status")

    numero_ordem_servico = fields.String(required=True)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)
    triagem = fields.Dict(required=True)
    diagnostico = fields.Dict(required=False)
    status = fields.String(required=False)

    def ajustando_datas_criacao_atualizacao(self, date):
        if isinstance(date, str):
            return datetime.now()
        else:
            return date


class AcessorioSchema(Schema):
    class Meta:
        model = equipamento_model.Acessorio
        fields = ("descricao", "acompanha", "quantidade", "estado_de_conservacao")

    descricao = fields.String(required=True)
    acompanha = fields.Boolean(required=True)
    quantidade = fields.Integer(required=True)
    estado_de_conservacao = fields.String(required=True)


class TriagemSchema(Schema):
    class Meta:
        model = equipamento_model.Triagem
        fields = ("nome_equipamento", "foto_equipamento_chegada", "tipo", "unidade_de_origem", "numero_do_patrimonio",
                  "numero_de_serie", "instituicao_de_origem", "nome_responsavel", "contato_responsavel",
                  "estado_de_conservacao", "fabricante", "marca", "modelo", "acessorios", "foto_apos_limpeza",
                  "observacao", "responsavel_pelo_preenchimento", "nome_instituicao_origem", "tipo_instituicao_origem",
                  "municipio_origem")

    nome_equipamento = fields.String(required=True)
    foto_equipamento_chegada = fields.String(required=True)
    tipo = fields.String(required=True)
    unidade_de_origem = fields.String(required=True)
    numero_do_patrimonio = fields.String(required=True)
    numero_de_serie = fields.String(required=True)
    instituicao_de_origem = fields.String(required=True)
    nome_responsavel = fields.String(required=True)
    contato_responsavel = fields.String(required=True)
    estado_de_conservacao = fields.String(required=True)
    fabricante = fields.String(required=True)
    marca = fields.String(required=True)
    modelo = fields.String(required=True)
    acessorios = fields.List(fields.Dict, required=True)
    foto_apos_limpeza = fields.String(required=True)
    observacao = fields.String(required=True)
    responsavel_pelo_preenchimento = fields.String(required=True)
    nome_instituicao_origem = fields.String(required=True)
    tipo_instituicao_origem = fields.String(required=True)
    municipio_origem = fields.String(required=True)


class DiagnosticoSchema(Schema):
    class Meta:
        model = equipamento_model.Triagem
        fields = ("resultado_tecnico", "demanda_servicos", "demanda_insumos", "acao_orientacao", "observacoes",
                  "itens")

    resultado_tecnico = fields.String(required=True)
    demanda_servicos = fields.String(required=True)
    demanda_insumos = fields.String(required=True)
    acao_orientacao = fields.String(required=True)
    observacoes = fields.String(required=True)
    #acessorios_extras = fields.List(fields.Dict, required=True)
    itens = fields.List(fields.Dict, required=True)


class AcessorioExtraSchema(Schema):
    class Meta:
        model = equipamento_model.AcessorioExtra
        fields = ("quantidade", "nome")

    quantidade = fields.Integer(required=True)
    nome = fields.String(required=True)

class ItemSchema(Schema):
    class Meta:
        model = equipamento_model.Item
        fields = ("nome", "tipo", "quantidade", "descricao", "valor", "prioridade", "unidade_medida")

    nome = fields.String(required=True)
    tipo = fields.String(required=True)
    quantidade = fields.Integer(required=True)
    descricao = fields.String(required=True)
    valor = fields.Float(required=True)
    prioridade = fields.String(required=True)
    unidade_medida = fields.String(required=True)

