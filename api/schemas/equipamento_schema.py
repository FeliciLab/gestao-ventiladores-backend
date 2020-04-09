from ..models import equipamento_model
from marshmallow import Schema, fields


class EquipamentoSchema(Schema):
    class Meta:
        model = equipamento_model.Equipamento
        fields = ("numero_ordem_servico", "data_hora", "triagem", "clinico", "tecnico", "foto_equipamento_chegada")

    numero_ordem_servico = fields.String(required=True)
    data_hora = fields.DateTime(required=True)
    triagem = fields.Dict(required=True)
    clinico = fields.Dict(required=False)
    tecnico = fields.Dict(required=False)

class TriagemSchema(Schema):
    class Meta:
        model = equipamento_model.Triagem
        fields = ("nome_equipamento", "foto_equipamento_chegada", "tipo", "unidade_de_origem", "numero_do_patrimonio",
                  "numero_de_serie", "instituicao_de_origem", "nome_responsavel", "contato_responsavel",
                  "estado_de_conservacao", "fabricante", "marca", "modelo", "acessorios", "foto_apos_limpeza",
                  "observacao", "responsavel_pelo_preenchimento")

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
    acessorios = fields.List(fields.String(), required=False)
    foto_apos_limpeza = fields.String(required=True)
    observacao = fields.String(required=False)
    responsavel_pelo_preenchimento = fields.String(required=False)

class ClinicoSchema(Schema):
    class Meta:
        model = equipamento_model.Clinico
        fields = ("classificao_ventilador", "resultados_do_teste", "acessorios_necessitados")

    classificao_ventilador = fields.String(required=True)
    resultados_do_teste = fields.String(required=True)
    acessorios_necessitados = fields.String(required=True)

class TecnicoSchema(Schema):
    class Meta:
        model = equipamento_model.Tecnico
        fields = ("resultado_do_teste", "demanda_por_insumo", "demanda_por_servico")

    resultado_do_teste = fields.String(required=True)
    demanda_por_insumo = fields.String(required=True)
    demanda_por_servico = fields.String(required=True)
