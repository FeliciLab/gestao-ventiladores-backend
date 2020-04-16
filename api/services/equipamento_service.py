from ..models import equipamento_model
from datetime import datetime
import random

def listar_equipamentos():
    return equipamento_model.Equipamento.objects().to_json()


def listar_equipamento_id(numero_ordem_servico):
    try:
        equipamento = equipamento_model.Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico)
        if not equipamento is None:
            return equipamento.to_json()
    except:
        return None


def listar_equipamento(id):
    try:
        equipamento = equipamento_model.Equipamento.objects.get(id=id)
        if not equipamento is None:
            return equipamento.to_json()
    except:
        return None


def registrar_equipamento(body):
    body['created_at'] = body.get('created_at', datetime.now())
    body['updated_at'] = body.get('updated_at', datetime.now())
    # Falta criar a situação onde as datas vem vazias, Exemplo: updated_at: ''
    return equipamento_model.Equipamento(**body).save().to_json()

def registrar_equipamento_foto(body):
    equipamento = equipamento_model.Equipamento()
    triagem = equipamento_model.Triagem()
    if 'foto_antes_limpeza' in body:
        triagem.foto_antes_limpeza = body['foto_antes_limpeza']
    else:
        triagem.foto_antes_limpeza = body['foto_apos_limpeza']
    equipamento.triagem = triagem
    equipamento.numero_ordem_servico = str(random.getrandbits(128))
    equipamento.created_at = datetime.now()
    equipamento.updated_at = datetime.now()
    return equipamento.save().to_json()

def atualizar_equipamento(atualizacao, numero_ordem_servico):
    equipamento_model.Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico).update(**atualizacao)

def atualizar_equipamento_id(atualizacao, id):
    equipamento_model.Equipamento.objects.get(id=id).update(**atualizacao)

def atualizar_foto_equipamento_id(atualizacao, id):
    equipamento = equipamento_model.Equipamento.objects.get(id=id)
    if 'foto_antes_limpeza' in atualizacao:
        equipamento.triagem.foto_antes_limpeza = atualizacao['foto_antes_limpeza']
    else:
        equipamento.triagem.foto_antes_limpeza = atualizacao['foto_apos_limpeza']
    equipamento.save()

def registrar_equipamento_foto(body):
    equipamento = equipamento_model.Equipamento()
    if 'foto_antes_limpeza' in body:
        equipamento.triagem.foto_antes_limpeza = body['foto_antes_limpeza']
    else:
        equipamento.triagem.foto_apos_limpeza = body['foto_apos_limpeza']
    equipamento.created_at = datetime.now()
    equipamento.updated_at = datetime.now()
    return equipamento.save().to_json()

def deletar_equipamento(numero_ordem_servico):
    equipamento_model.Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico).delete()


def lista_equipamentos_status(status):
    return equipamento_model.Equipamento.objects(status=status).to_json()

def registrar_equipamento_vazio():
    equipamento = equipamento_model.Equipamento()
    equipamento.numero_ordem_servico = str(random.getrandbits(128))
    triagem = equipamento_model.Triagem()
    equipamento.triagem = triagem
    return equipamento.save()

def adicionar_marca_modelo_fabricante():
    pass
