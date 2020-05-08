from api.models.equipamento_model import Equipamento
from config.db import db
from datetime import datetime


class Acessorio(db.EmbeddedDocument):
    descricao = db.StringField(required=False)
    acompanha = db.BooleanField(required=False)
    quantidade = db.IntField(required=False)
    estado_de_conservacao = db.StringField(required=False)


class Triagem(db.EmbeddedDocument):
    estado_de_conservacao = db.StringField(required=False)
    acessorios = db.EmbeddedDocumentListField(Acessorio, required=False)
    foto_antes_limpeza = db.StringField(required=False)
    foto_apos_limpeza = db.StringField(required=False)

class Item(db.EmbeddedDocument):
    tipo = db.StringField(required=False)
    fabricante = db.StringField(required=False)
    codigo = db.StringField(required=False)
    nome = db.StringField(required=False)
    unidade_medida = db.StringField(required=False)
    quantidade = db.IntField(required=False)
    descricao = db.StringField(required=False)

class Diagnostico(db.EmbeddedDocument):
    resultado_tecnico = db.StringField(required=False)
    demanda_servicos = db.StringField(required=False)
    observacoes = db.StringField(required=False)
    itens = db.EmbeddedDocumentListField(Item, required=False)


class OrdemServico(db.Document):
    equipamento_id = db.ReferenceField(Equipamento)
    numero_ordem_servico = db.StringField(required=False, unique=True)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    updated_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    status = db.StringField(required=False)
    triagem = db.EmbeddedDocumentField(Triagem, required=False)
    diagnostico = db.EmbeddedDocumentField(Diagnostico, required=False)
