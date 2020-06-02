from config.db import db
from datetime import datetime

class Item(db.Document):
    tipo = db.StringField(required=False)
    fabricante = db.StringField(required=False)
    codigo = db.StringField(required=False)
    nome = db.StringField(required=False)
    unidade_medida = db.StringField(required=False)
    quantidade = db.IntField(required=False)
    descricao = db.StringField(required=False)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    updated_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    deleted_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    