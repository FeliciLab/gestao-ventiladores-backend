from config.db import db
from datetime import datetime


class Acessorio(db.EmbeddedDocument):
    descricao = db.StringField(required=False)
    acompanha = db.BooleanField(required=False)
    quantidade = db.IntField(required=False)
    estado_de_conservacao = db.StringField(required=False)


class Triagem(db.EmbeddedDocument):
    #numero_de_serie = db.StringField(required=False)
    #nome_equipamento = db.StringField(required=False)
    #numero_do_patrimonio = db.StringField(required=False)
    # tipo = db.StringField(required=False)
    # marca = db.StringField(required=False)
    # modelo = db.StringField(required=False)
    # fabricante = db.StringField(required=False)
    # municipio_origem = db.StringField(required=False)
    # nome_instituicao_origem = db.StringField(required=False)
    # tipo_instituicao_origem = db.StringField(required=False)
    # nome_responsavel = db.StringField(required=False)
    #contato_responsavel = db.StringField(required=False)
    estado_de_conservacao = db.StringField(required=False)
    acessorios = db.EmbeddedDocumentListField(Acessorio, required=False)
    foto_antes_limpeza = db.StringField(required=False)
    foto_apos_limpeza = db.StringField(required=False)

class Item(db.EmbeddedDocument):
    quantidade = db.IntField(required=True)
    nome = db.StringField(required=True)
    tipo = db.StringField(required=True)
    descricao = db.StringField(required=True)
    valor = db.FloatField(required=True)
    prioridade = db.StringField(required=True)
    unidade_medida = db.StringField(required=True)


class Diagnostico(db.EmbeddedDocument):
    resultado_tecnico = db.StringField(required=False)
    demanda_servicos = db.StringField(required=False)
    demanda_insumos = db.StringField(required=False)
    acao_orientacao = db.StringField(required=False)
    observacoes = db.StringField(required=False)
    itens = db.EmbeddedDocumentListField(Item, required=False)


class Equipamento(db.Document):
    numero_ordem_servico = db.StringField(required=False, unique=True)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    updated_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    status = db.StringField(required=False)
    # FORMULARIO DE TRIAGEM DE EQUIPAMENTO
    triagem = db.EmbeddedDocumentField(Triagem, required=False)
    # FORMULARIO DE DIAGNOSTICO DE EQUIPAMENTO
    diagnostico = db.EmbeddedDocumentField(Diagnostico, required=False)



