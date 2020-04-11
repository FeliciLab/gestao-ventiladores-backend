from config.db import db


class MarcasFabricante(db.EmbeddedDocument):
    marca = db.StringField(required=True)
    modelos = db.ListField(db.StringField(),required=True)

class Fabricante(db.Document):
    # TODO pegar o pdf lista pecas dentro da pasta CentralDeVentiladores e pegar os dados de fabricante com seus modelos
    # para poder gerar alguns dados enquanto a gente nao recebe o csv para da uma carga no banco de dados
    fabricante_nome = db.StringField(required=True, unique=True)
    marcas = db.EmbeddedDocumentListField(MarcasFabricante, required=True)
