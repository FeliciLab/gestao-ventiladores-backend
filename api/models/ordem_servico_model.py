from datetime import datetime

from api.models.equipamento_model import Equipamento
from config.db import db


class Acessorio(db.EmbeddedDocument):
    descricao = db.StringField(required=True)
    acompanha = db.BooleanField(required=True)
    quantidade = db.IntField(required=True)
    estado_de_conservacao = db.StringField(required=True)


class Triagem(db.EmbeddedDocument):
    estado_de_conservacao = db.StringField(required=True)
    acessorios = db.EmbeddedDocumentListField(Acessorio, required=True)
    foto_antes_limpeza = db.StringField(required=True)
    foto_apos_limpeza = db.StringField(required=True)

class Item(db.EmbeddedDocument):
    tipo = db.StringField(required=True)
    fabricante = db.StringField(required=True)
    codigo = db.StringField(required=True)
    nome = db.StringField(required=True)
    unidade_medida = db.StringField(required=True)
    quantidade = db.IntField(required=True)
    descricao = db.StringField(required=True)


class Diagnostico(db.EmbeddedDocument):
    resultado_tecnico = db.StringField(required=True)
    demanda_servicos = db.StringField(required=True)
    demanda_insumos = db.StringField(required=True)
    acao_orientacao = db.StringField(required=True)
    observacoes = db.StringField(required=True)
    itens = db.EmbeddedDocumentListField(Item, required=True)


class OrdemServico(db.Document):
    equipamento_id = db.ReferenceField(Equipamento)
    numero_ordem_servico = db.StringField(required=True, unique=True)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=True)
    updated_at = db.DateTimeField(default=datetime.utcnow(), required=True)
    status = db.StringField(required=True)

    # FORMULARIO DE TRIAGEM DE EQUIPAMENTO
    triagem = db.EmbeddedDocumentField(Triagem, required=True)
    # FORMULARIO DE DIAGNOSTICO DE EQUIPAMENTO
    diagnostico = db.EmbeddedDocumentField(Diagnostico, required=True)
