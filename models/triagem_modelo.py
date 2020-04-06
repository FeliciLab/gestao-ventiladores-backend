from config.db import db

class Equipamento(db.EmbeddedDocument):
    foto_equipamento_chegada = db.StringField()  # verificar se tem um tipo especifico para links, faz sentido ser único ?
    tipo = db.StringField(required=True)
    unidade_de_origem = db.StringField(required=True)
    numero_do_patrimonio = db.StringField(required=True)
    numero_de_serie = db.StringField(required=True)
    instituicao_de_origem = db.StringField(required=True)
    responsavel_contato_da_instituicao_de_origem = db.StringField(required=True)
    estado_de_conservacao = db.StringField(required=True)
    marca = db.StringField(required=True)
    modelo = db.StringField(required=True)
    acessorios = db.StringField(required=True)
    foto_apos_limpeza = db.StringField()
    observacao = db.StringField()
    responsavel_pelo_preenchimento = db.StringField(required=True)

class AcaoAvaliacao(db.EmbeddedDocument):
    descricao_acao = db.StringField(required=True)
    passou = db.BooleanField(required=True)
    descricao_da_avaliacao = db.StringField()

class Clinico(db.EmbeddedDocument):
    acoes_avaliacao = db.ListField(db.EmbeddedDocumentField(AcaoAvaliacao))
    informar_os_resultados_do_teste = db.StringField()

class Tecnico(db.EmbeddedDocument):
    defeito_observado = db.StringField()
    acoes_necessarias = db.StringField()


class Triagem(db.Document):
    numero_ordem_servico = db.StringField(required=True, unique=True)
    # FORMULARIO DE TRIAGEM DE EQUIPAMENTO
    equipamento = db.EmbeddedDocumentField(Equipamento)
    # FORMULARIO DE DIAGNOSTICO CLINICO
    clinico = db.EmbeddedDocumentField(Clinico, required=False)
    # FORMULARIO DE DIAGNOSTICO TECNICO
    tecnico = db.EmbeddedDocumentField(Tecnico, required=False)
