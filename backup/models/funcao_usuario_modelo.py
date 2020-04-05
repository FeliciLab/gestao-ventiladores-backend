from config.db import db


class FuncaoUsuario(db.Document):
    tipo_de_funcao_do_usuario = db.StringField(required=True, unique=True)
