from api.models import equipamento_model


def listar_equipamentos():
    return equipamento_model.Equipamento.objects()

def listar_equipamento_by_id(_id):
    return equipamento_model.Equipamento.objects(id=_id).first()


def consultar_numero_de_serie(numero_de_serie):
    return equipamento_model.Equipamento.objects(
        numero_de_serie=numero_de_serie
    ).only(
        'id', 'numero_de_serie'
    ).first()

def listar_equipamento_by_numero_de_serie(numero_de_serie):
    try:
        equipamento = equipamento_model.Equipamento.objects.get(numero_de_serie=numero_de_serie)
    except:
        equipamento = None
    finally:
        return equipamento


def registar_equipamento(body):
    equipamento = equipamento_model.Equipamento(**body).save()
    return str(equipamento.id)


def atualizar_equipamento(atualizacao, _id):
    equipamento_model.Equipamento.objects.get(id=_id).update(**atualizacao)


def deletar_equipamento(_id):
    equipamento_model.Equipamento.objects.get(id=_id).delete()
