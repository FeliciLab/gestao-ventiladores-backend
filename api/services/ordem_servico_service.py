from ..models import ordem_servico_model
from datetime import datetime


def listar_ordem_servico():
    return ordem_servico_model.OrdemServico.objects().to_json()


# def listar_ordem_servico_by_numero_ordem_servico(numero_ordem_servico):
#     try:
#         ordem_servico = ordem_servico_model.OrdemServico.objects.get(numero_ordem_servico=numero_ordem_servico)
#         if not ordem_servico is None:
#             return ordem_servico.to_json()
#     except:
#         return None


def listar_ordem_servico_by_id(_id):
    try:
        ordem_servico = ordem_servico_model.OrdemServico.objects.get(id=_id)
        if not ordem_servico is None:
            return ordem_servico.to_json()
    except:
        return None

def listar_ordem_servico_by_numero_ordem_servico(ordem_servico):
    try:
        ordem_servico = ordem_servico_model.OrdemServico.objects.get(ordem_servico=ordem_servico).to_json()
        if not ordem_servico is None:
            return ordem_servico
    except:
        return None

def filtering_ordem_servico_queries(query):
    ordem_servico_model.OrdemServico.objects()


def registrar_ordem_servico(body):
    body['created_at'] = body.get('created_at', datetime.now())
    body['updated_at'] = body.get('updated_at', datetime.now())
    # Falta criar a situação onde as datas vem vazias, Exemplo: updated_at: ''
    return ordem_servico_model.OrdemServico(**body).save()



# def atualizar_ordem_servico(atualizacao, numero_ordem_servico):
#     ordem_servico_model.OrdemServico.objects.get(id=numero_ordem_servico).update(**atualizacao)


def atualizar_ordem_servico(_id, atualizacao):
     ordem_servico_model.OrdemServico.objects.get(id=_id).update(**atualizacao)


def atualizar_ordem_servico_importacao(_id, atualizacao):
    return ordem_servico_model.OrdemServico.objects.get(id=_id).update(
        numero_ordem_servico=atualizacao['numero_ordem_servico'],
        created_at=atualizacao['created_at'],
        updated_at=atualizacao['updated_at'],
        status=atualizacao['status'],
        triagem=atualizacao['triagem']
    )


def atualizar_foto_equipamento(_id, atualizacao):
    ordem_servico = ordem_servico_model.OrdemServico.objects.get(id=_id)
    if 'foto_antes_limpeza' in atualizacao:
        ordem_servico .triagem.foto_antes_limpeza = atualizacao['foto_antes_limpeza']
    else:
        ordem_servico .triagem.foto_antes_limpeza = atualizacao['foto_apos_limpeza']
    ordem_servico.save()


def registrar_equipamento_foto(body):
    ordem_servico = ordem_servico_model.OrdemServico()
    if 'foto_antes_limpeza' in body:
        ordem_servico.triagem.foto_antes_limpeza = body['foto_antes_limpeza']
    else:
        ordem_servico.triagem.foto_apos_limpeza = body['foto_apos_limpeza']
    ordem_servico.created_at = datetime.now()
    ordem_servico.updated_at = datetime.now()
    return ordem_servico.save()

# todo Denis, eu acabei apagando esse metodo pq eu n vi ele sendo utilizado. Verificar
# def registrar_equipamento_foto(body):
#     equipamento = ordem_servico_model.OrdemServico()
#     triagem = ordem_servico_model.Triagem()
#     if 'foto_antes_limpeza' in body:
#         triagem.foto_antes_limpeza = body['foto_antes_limpeza']
#     else:
#         triagem.foto_antes_limpeza = body['foto_apos_limpeza']
#     equipamento.triagem = triagem
#     equipamento.numero_ordem_servico = str(random.getrandbits(128))
#     equipamento.created_at = datetime.now()
#     equipamento.updated_at = datetime.now()
#     return equipamento.save().to_json()


def deletar_ordem_servico(_id):
    ordem_servico_model.OrdemServico.objects.get(id=_id).delete()


def listar_ordem_servico_status(status):
    return ordem_servico_model.OrdemServico.objects(status=status).to_json()


def registrar_equipamento_vazio():
    ordem_servico = ordem_servico_model.OrdemServico()
    triagem = ordem_servico_model.Triagem()
    ordem_servico.triagem = triagem
    return ordem_servico.save()

