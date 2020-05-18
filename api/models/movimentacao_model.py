from api.models.equipamento_model import Equipamento
from config.db import db
from datetime import datetime


class Movimentacao(db.Document):
    codigo = db.StringField(required=False, unique=False)
    tipo = db.StringField(required=False, unique=False)
    equipamentos_id = db.ListField(db.ReferenceField(Equipamento))
    instituicao_destino = db.StringField(required=False, unique=False)
    cidade_destino = db.StringField(required=False, unique=False)
    cnpj_destino = db.StringField(required=False, unique=False)
    endereco_destino = db.StringField(required=False, unique=False)
    nome_responsavel_destino = db.StringField(required=False, unique=False)
    contato_responsavel_destino = db.StringField(required=False, unique=False)
    nome_responsavel_transporte = db.StringField(required=False, unique=False)
    contato_responsavel_transporte = db.StringField(required=False,
                                                    unique=False)
    data_entrega = db.DateTimeField(required=False)
    acessorios = db.DictField(requried=False)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    updated_at = db.DateTimeField(default=datetime.utcnow(), required=False)
