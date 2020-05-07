from ..models import ordem_servico_model
from ..models.equipamento_model import Equipamento
from bson import ObjectId
from bson.json_util import dumps
from datetime import datetime
from ..utils import query_parser
from ..services import equipamento_service


def listar_ordem_servico():
    pipeline = [
        {
            "$lookup": {
                "from": Equipamento._get_collection_name(),
                "localField": "equipamento_id",
                "foreignField": "_id",
                "as": "equipamento"
            }
        }
    ]

    docs = []
    for ordem in ordem_servico_model.OrdemServico.objects(
            status__ne='tmp').aggregate(pipeline):
        docs.append(ordem)

    return dumps(docs)


def listar_ordem_servico_by_id(_id):
    return ordem_servico_model.OrdemServico.objects.get(id=_id)


def listar_ordem_servico_by_numero_ordem_servico(numero_ordem_servico):
    return ordem_servico_model.OrdemServico.objects(
        numero_ordem_servico=numero_ordem_servico).first()


def ordem_servico_queries(body):
    parsed_query_dt = query_parser.parse(body["where"])

    if not "select" in body:
        body["select"] = []

    filted_ordem_servico_list = ordem_servico_model.OrdemServico.objects(
        __raw__=parsed_query_dt).only(*body["select"])

    return filted_ordem_servico_list.to_json()


def registrar_ordem_servico(body):
    # eu acho que isso nao deveria ficar aqui entro by Lucas
    body['created_at'] = body.get('created_at', datetime.now())
    body['updated_at'] = body.get('updated_at', datetime.now())
    # Falta criar a situação onde as datas vem vazias, Exemplo: updated_at: ''
    return ordem_servico_model.OrdemServico(**body).save()


def atualizar_ordem_servico(_id, atualizacao):
    # isso nao deve ficar aqui dentro by Lucas

    # if 'equipamento_id' in atualizacao:
    #     equipamento = equipamento_service.listar_equipamento_by_id(atualizacao['equipamento_id'])
    #     atualizacao['equipamento_id'] = equipamento

    ordem_servico_model.OrdemServico.objects.get(id=_id).update(**atualizacao)


def atualizar_ordem_servico_importacao(_id, atualizacao):
    ordem_servico = listar_ordem_servico_by_numero_ordem_servico(
        atualizacao['numero_ordem_servico'])
    ordem_servico.triagem = atualizacao['triagem']
    return ordem_servico_model.OrdemServico.objects.get(id=_id).update(
        equipamento_id=atualizacao['equipamento_id'],
        numero_ordem_servico=atualizacao['numero_ordem_servico'],
        created_at=atualizacao['created_at'],
        updated_at=atualizacao['updated_at'],
        status=atualizacao['status'],
        triagem=ordem_servico.triagem
    )


def atualizar_foto_equipamento(_id, atualizacao):
    ordem_servico = ordem_servico_model.OrdemServico.objects.get(id=_id)
    if 'foto_antes_limpeza' in atualizacao:
        ordem_servico.triagem.foto_antes_limpeza = atualizacao[
            'foto_antes_limpeza']
    else:
        ordem_servico.triagem.foto_antes_limpeza = atualizacao[
            'foto_apos_limpeza']
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


def deletar_ordem_servico(_id):
    ordem_servico_model.OrdemServico.objectsget(id=_id).delete()


def listar_ordem_servico_status(status):
    return ordem_servico_model.OrdemServico.objects(status=status)


def atualizar_foto_ordem_servico(_id, atualizacao):
    ordem_servico = listar_ordem_servico_by_id(_id)
    if atualizacao['triagem']['foto_apos_limpeza'] is "":
        ordem_servico.triagem.foto_antes_limpeza = atualizacao['triagem'][
            'foto_antes_limpeza']
        ordem_servico_model.OrdemServico.objects.get(id=_id).update(
            triagem=ordem_servico.triagem
        )
    else:
        ordem_servico.triagem.foto_apos_limpeza = atualizacao['triagem'][
            'foto_apos_limpeza']
        ordem_servico_model.OrdemServico.objects.get(id=_id).update(
            triagem=ordem_servico.triagem
        )


def registrar_equipamento_vazio():
    id = ObjectId()
    ordem_servico = ordem_servico_model.OrdemServico()
    ordem_servico.numero_ordem_servico = 'tmp_' + str(id)
    ordem_servico.id = id
    triagem = ordem_servico_model.Triagem()
    ordem_servico.triagem = triagem
    ordem_servico.status = 'tmp'
    return ordem_servico.save()


def deserealize_ordem_servico(body):
    ordem_servico = ordem_servico_model.OrdemServico()

    for att_name, att_value in body.items():
        if "equipamento_id" is att_name:
            for equipamento in body["equipamento_id"]:
                equipamento.equipamento_id = (equipamento.id)

        elif "created_at" is att_name:
            ordem_servico.created_at = datetime.strptime(body["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

        elif "created_at" is att_name:
            ordem_servico.created_at = datetime.strptime(body["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        else:
            try:
                setattr(ordem_servico, att_name, att_value)
            except:
                continue

    return ordem_servico

    # ordem_servico = ordem_servico_model.OrdemServico()
    # if "numero_ordem_servico" in body: ordem_servico.numero_ordem_servico = body["numero_ordem_servico"]
    # if "equipamento_id" in body: ordem_servico.equipamento_id = body["equipamento_id"].id
    # if "created_at" in body: ordem_servico.created_at = datetime.strptime(body["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
    # if "updated_at" in body: ordem_servico.updated_at = datetime.strptime(body["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
    # if "status" in body: ordem_servico.status = body["status"]
    # if "triagem" in body: ordem_servico.triagem = body["triagem"]
    # if "diagnostico" in body: ordem_servico.diagnostico = body["diagnostico"]
    # return ordem_servico
