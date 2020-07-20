from config.db import db
from datetime import datetime


class Equipamento(db.Document):
    meta = {'collection': 'equipamento'}

    numero_de_serie = db.StringField(required=True)
    nome_equipamento = db.StringField(required=False)
    status = db.StringField(required=False)
    numero_do_patrimonio = db.StringField(required=False)
    tipo = db.StringField(required=False)
    marca = db.StringField(required=False)
    modelo = db.StringField(required=False)
    fabricante = db.StringField(required=False)
    municipio_origem = db.StringField(required=False)
    nome_instituicao_origem = db.StringField(required=False)
    tipo_instituicao_origem = db.StringField(required=False)
    nome_responsavel = db.StringField(required=False)
    contato_responsavel = db.StringField(required=False)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    updated_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    deleted_at = db.DateTimeField(required=False)

