from ..models import equipamento_model
from datetime import datetime


def listar_equipamentos():
    return equipamento_model.Equipamento.objects().to_json()


def listar_equipamento_id(numero_ordem_servico):
    try:
        equipamento = equipamento_model.Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico)
        if not equipamento is None:
            return equipamento.to_json()
    except:
        return None


def registrar_equipamento(body):
    body['created_at'] = body.get('created_at', datetime.now())
    body['updated_at'] = body.get('updated_at', datetime.now())
    # Falta criar a situação onde as datas vem vazias, Exemplo: updated_at: ''
    return equipamento_model.Equipamento(**body).save().to_json()


def atualizar_equipamento(atualizacao, numero_ordem_servico):
    equipamento_model.Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico).update(**atualizacao)


def deletar_equipamento(numero_ordem_servico):
    equipamento_model.Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico).delete()


def lista_equipamentos_status(status):
    return equipamento_model.Equipamento.objects(status=status).to_json()


def adicionar_marca_modelo_fabricante():
    pass
