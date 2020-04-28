from config.db import db


class OrdemCompra(db.Document):
    meta = {'collection': 'ordem_compra'}

    numero_ordem_compra = db.StringField(required=False, unique=True)
    itens = db.ListField(required=False)

