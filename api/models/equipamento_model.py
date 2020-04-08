from config.db import db
from datetime import datetime

class Triagem(db.EmbeddedDocument):
    foto_equipamento_chegada = db.ListField(required=True)  # verificar se tem um tipo especifico para links, faz sentido ser único ?
    tipo = db.StringField(required=True)
    unidade_de_origem = db.StringField(required=True)
    numero_do_patrimonio = db.StringField(required=True)
    numero_de_serie = db.StringField(required=True)
    instituicao_de_origem = db.StringField(required=True)
    responsavel_contato_da_instituicao_de_origem = db.StringField(required=True)
    estado_de_conservacao = db.StringField(required=True)
    fabricante = db.StringField(required=True)
    marca = db.StringField(required=True)
    modelo = db.StringField(required=True)
    acessorios = db.ListField(required=True)
    foto_apos_limpeza = db.ListField(required=True)
    observacao = db.StringField(required=False)
    responsavel_pelo_preenchimento = db.StringField(required=False) # Responsável pelo preenchimento deve ser false?

class AcaoAvaliacao(db.EmbeddedDocument):
    descricao_acao = db.StringField(required=True)
    passou = db.BooleanField(required=True)
    descricao_da_avaliacao = db.StringField(required=False)

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
    data_hora = db.DateTimeField(default=datetime.utcnow)
    # FORMULARIO DE TRIAGEM DE EQUIPAMENTO
    triagem = db.EmbeddedDocumentField(Triagem, required=True)
    # FORMULARIO DE DIAGNOSTICO CLINICO
    clinico = db.EmbeddedDocumentField(Clinico, required=False)
    # FORMULARIO DE DIAGNOSTICO TECNICO
    tecnico = db.EmbeddedDocumentField(Tecnico, required=False)
