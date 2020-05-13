from datetime import datetime

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


def registar_equipamento_complete(body):
    return equipamento_model.Equipamento(**body).save()


def atualizar_equipamento(atualizacao, _id):
    equipamento_model.Equipamento.objects.get(id=_id).update(**atualizacao)


def deletar_equipamento(_id):
    equipamento_model.Equipamento.objects.get(id=_id).delete()



def deserealize_equipamento(body):
    equipamento = equipamento_model.Equipamento()

    for att_name, att_value in body.items():

        if "created_at" is att_name:
            equipamento.created_at = datetime.strptime(body["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

        if "created_at" is att_name:
            equipamento.created_at = datetime.strptime(body["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        else:
            try:
                setattr(equipamento, att_name, att_value)
            except:
                continue

    return equipamento
