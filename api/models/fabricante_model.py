from config.db import db


class MarcasFabricante(db.EmbeddedDocument):
    marca = db.StringField(required=True)
    modelos = db.ListField(db.StringField(), required=True)


class Fabricante(db.Document):
    fabricante_nome = db.StringField(required=True, unique=True)
    marcas = db.EmbeddedDocumentListField(MarcasFabricante, required=True)
