from config.db import db


class Equipamento(db.Document):
    # FORMULARIO DE TRIAGEM DE EQUIPAMENTO

    numero_ordem_servico = db.StringField(required=True, unique=True)
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

    # FORMULARIO DE DIAGNOSTICO CLINICO
    acoes_avaliacao = db.ListField(db.DictField(), required=False)
    informar_os_resultados_do_teste = db.StringField()

    # FORMULARIO DE DIAGNOSTICO TECNICO
    defeito_observado = db.StringField()
    acoes_necessarias = db.StringField()
