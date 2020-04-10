from config.db import db
from datetime import datetime

class Acessorio(db.EmbeddedDocument):
    descricao = db.StringField(required=True)
    acompanha = db.BooleanField(required=True)
    quantidade = db.IntField(required=True)
    estado_de_conservacao = db.StringField(required=True)

class Triagem(db.EmbeddedDocument):
    nome_equipamento = db.StringField(required=True)
    foto_equipamento_chegada = db.StringField(required=True)
    tipo = db.StringField(required=True)
    unidade_de_origem = db.StringField(required=True)
    numero_do_patrimonio = db.StringField(required=True)
    numero_de_serie = db.StringField(required=True)
    instituicao_de_origem = db.StringField(required=True)
    nome_responsavel = db.StringField(required=True)
    contato_responsavel = db.StringField(required=True)
    estado_de_conservacao = db.StringField(required=True)
    fabricante = db.StringField(required=True)
    marca = db.StringField(required=True)
    modelo = db.StringField(required=True)
    acessorios = db.EmbeddedDocumentListField(Acessorio, required=False)
    foto_apos_limpeza = db.StringField(required=True)
    observacao = db.StringField(required=False)
    responsavel_pelo_preenchimento = db.StringField(required=False)

class Clinico(db.EmbeddedDocument):
    classificao_ventilador = db.StringField(required=False)
    resultados_do_teste = db.StringField(required=False)
    acessorios_necessitados = db.StringField(required=False)

class Tecnico(db.EmbeddedDocument):
    resultado_do_teste = db.StringField(required=False)
    demanda_por_insumo = db.StringField(required=False)
    demanda_por_servico = db.StringField(required=False)

class Equipamento(db.Document):
    numero_ordem_servico = db.StringField(required=True, unique=True)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    updated_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    status = db.StringField(required=False)
    # FORMULARIO DE TRIAGEM DE EQUIPAMENTO
    triagem = db.EmbeddedDocumentField(Triagem, required=True)
    # FORMULARIO DE DIAGNOSTICO CLINICO
    clinico = db.EmbeddedDocumentField(Clinico, required=False)
    # FORMULARIO DE DIAGNOSTICO TECNICO
    tecnico = db.EmbeddedDocumentField(Tecnico, required=False)
