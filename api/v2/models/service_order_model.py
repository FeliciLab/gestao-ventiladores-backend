from api.models.equipamento_model import Equipamento
from api.v2.models.item_model import Item
from config.db import db
from datetime import datetime


class Acessorio(db.EmbeddedDocument):
    item_id = db.ReferenceField(Item, required=False)
    acompanha = db.BooleanField(required=False)
    quantidade = db.IntField(required=False)
    estado_de_conservacao = db.StringField(required=False)


class Triagem(db.EmbeddedDocument):
    estado_de_conservacao = db.StringField(required=False)
    acessorios = db.EmbeddedDocumentListField(Acessorio, required=False)
    foto_antes_limpeza = db.StringField(required=False)
    foto_apos_limpeza = db.StringField(required=False)


class ItemDiagnostico(db.EmbeddedDocument):
    item_id = db.ReferenceField(Item, required=False)
    quantidade = db.IntField(required=False)


class Diagnostico(db.EmbeddedDocument):
    resultado_tecnico = db.StringField(required=False)
    demanda_servicos = db.StringField(required=False)
    observacoes = db.StringField(required=False)
    itens = db.EmbeddedDocumentListField(ItemDiagnostico, required=False)


class Calibragem(db.EmbeddedDocument):
    status = db.StringField(required=False)


class OrdemServico(db.Document):
    equipamento_id = db.ReferenceField(Equipamento)
    numero_ordem_servico = db.StringField(required=False, unique=True)
    status = db.StringField(required=False)
    triagem = db.EmbeddedDocumentField(Triagem, required=False)
    diagnostico = db.EmbeddedDocumentField(Diagnostico, required=False)
    calibragem = db.EmbeddedDocumentField(Calibragem, required=False)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    updated_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    deleted_at = db.DateTimeField(required=False)
