from datetime import datetime
from bson.json_util import dumps
import json
from api.models import movimentacao_model
from api.models.equipamento_model import Equipamento
from api.models.movimentacao_model import Movimentacao
from api.utils import query_parser
from api.utils.descerialization_data_model_patch import \
    deserialize_body_to_model


def listar_movimentacoes():
    pipeline = [
        {
            "$lookup": {
                "from": Equipamento._get_collection_name(),
                "localField": "equipamentos_id",
                "foreignField": "_id",
                "as": "equipamentos",
            }
        }
    ]

    docs = []
    for data in movimentacao_model.Movimentacao.objects().aggregate(pipeline):
        docs.append(data)

    return dumps(docs)


def listar_movimentacao_id(_id):
    try:
        movimentacao = movimentacao_model.Movimentacao.objects.get(id=_id)
    except Exception:
        movimentacao = None
    finally:
        return movimentacao


def registar_movimentacao(body):
    """
        Registra uma nova movimentação, gerando o próprio código baseado
        no último código registrado no banco.
    """
    ultimo_documento = json.loads(
        movimentacao_model.Movimentacao.objects.order_by("-codigo").to_json()
    )
    codigo_ultimo_documento = (
        0 if len(ultimo_documento) == 0 else int(ultimo_documento[0]["codigo"])
    )
    codigo = str(codigo_ultimo_documento + 1).zfill(4)
    body["codigo"] = codigo

    return movimentacao_model.Movimentacao(**body).save()


def atualizar_movimentacao(_id, atualizacao):
    movimentacao_model.Movimentacao.objects.get(id=_id).update(**atualizacao)


def deletar_movimentacao(_id):
    movimentacao_model.Movimentacao.objects.get(id=_id).delete()


def movimentacao_queries(body):
    parsed_query_dt = query_parser.parse(body["where"])

    if "select" not in body:
        body["select"] = []

    filted_movimentacao_list = movimentacao_model.Movimentacao.objects(
        __raw__=parsed_query_dt
    ).only(*body["select"])

    return filted_movimentacao_list.to_json()


def deserialize_movimentacao_service(body):
    return deserialize_body_to_model(
        body=body,
        model=Movimentacao(),
        custom_deserialize=custom_deserialize
    )


def custom_deserialize(body, att_name):
    if "equipamentos_id" == att_name:
        data = []
        for equipamento in body["equipamentos_id"]:
            data.append(equipamento.id)

        return data

    return None
