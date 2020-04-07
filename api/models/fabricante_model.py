from config.db import db


class Fabricante(db.Document):
    # TODO pegar o pdf lista pecas dentro da pasta CentralDeVentiladores e pegar os dados de fabricante com seus modelos
    # para poder gerar alguns dados enquanto a gente nao recebe o csv para da uma carga no banco de dados
    fabricante_nome = db.StringField(required=True, unique=True)
    modelo = db.ListField(required=True, unique=True)
