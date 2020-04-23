from config.db import db


class OrdemCompra(db.Document):
    numero_ordem_compra = db.StringField(required=False, unique=True)
    itens = db.ListField(required=False)

