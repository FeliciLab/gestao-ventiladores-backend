from config.db import db

class Item(db.EmbeddedDocument):
    tipo = db.StringField(required=False)
    nome_item = db.StringField(required=False)
    descricao_item = db.StringField(required=False)
    unidade = db.StringField(required=False)
    quantidade = db.IntField(required=False)
    fabricante = db.StringField(required=False)
    codigo_item = db.StringField(required=False)

class OrdemCompra(db.EmbeddedDocument):
    numero_ordem_compra = db.StringField(required=False, unique=True)
    itens = db.EmbeddedDocumentListField(Item, required=False)

