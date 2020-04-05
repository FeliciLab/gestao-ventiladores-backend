from config.db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Usuario(db.Document):
    nome = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    senha = db.StringField(required=True, min_length=6)
    categoria = db.StringField(required=True) # Por enquanto é String
    rg = db.IntField(required=True)
    cpf = db.IntField(required=True)


    def gera_hash(self):
        self.senha = generate_password_hash(self.senha).decode('utf8')

    def verifica_senha(self, senha):
        return check_password_hash(self.senha, senha)