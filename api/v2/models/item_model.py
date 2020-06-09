from config.db import db
from datetime import datetime

class Item(db.Document):
    tipo = db.StringField(required=False)
    fabricante = db.StringField(required=False)
    codigo = db.StringField(required=False)
    nome = db.StringField(required=True)
    unidade_medida = db.StringField(required=True)
    quantidade = db.IntField(required=True)
    descricao = db.StringField(required=False)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    updated_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    deleted_at = db.DateTimeField(required=False)
