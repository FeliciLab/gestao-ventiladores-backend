from ..models import equipamento_model

def listar_equipamentos():
    return equipamento_model.Equipamento.objects().to_json()

def listar_equipamento_id(numero_ordem_servico):
    try:
        equipamento = equipamento_model.Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico).to_json()
    except:
        equipamento = None
    finally:
        return equipamento

def registrar_equipamento(body):
    return equipamento_model.Equipamento(**body).save().to_json()

def atualizar_equipamento(atualizacao, numero_ordem_servico):
    equipamento_model.Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico).update(**atualizacao)

def deletar_equipamento(numero_ordem_servico):
    equipamento_model.Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico).delete()