from config.db import db
from datetime import datetime
from ..models.ordem_servico_model import Item


class OrdemCompra(db.Document):
    meta = {'collection': 'ordem_compra'}

    numero_ordem_compra = db.StringField(required=False, unique=True)
    itens = db.EmbeddedDocumentListField(Item, required=False)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    updated_at = db.DateTimeField(default=datetime.utcnow(), required=False)
