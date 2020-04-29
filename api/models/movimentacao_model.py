from api.models.equipamento_model import Equipamento
from config.db import db


class Movimentacao(db.Document):
    tipo = db.StringField(required=False, unique=False)
    equipamento_id = db.ReferenceField(Equipamento)
    instituicao_destino = db.StringField(required=False, unique=False)
    cidade_destino = db.StringField(required=False, unique=False)
    cnpj_destino = db.StringField(required=False, unique=False)
    endereco_destino = db.StringField(required=False, unique=False)
    nome_responsavel_destino = db.StringField(required=False, unique=False)
    contato_responsavel_destino = db.StringField(required=False, unique=False)
    nome_responsavel_transporte = db.StringField(required=False, unique=False)
    contato_responsavel_transporte = db.StringField(required=False, unique=False)
