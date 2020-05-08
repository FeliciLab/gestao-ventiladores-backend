from datetime import datetime
from bson.json_util import dumps
import json
from api.models import movimentacao_model
from api.models.equipamento_model import Equipamento
from api.models.movimentacao_model import Movimentacao
from api.utils import query_parser


def listar_movimentacoes():
    pipeline = [
        {
            "$lookup": {
                "from": Equipamento._get_collection_name(),
                "localField": "equipamentos_id",
                "foreignField": "_id",
                "as": "equipamentos"
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
    except:
        movimentacao = None
    finally:
        return movimentacao


def registar_movimentacao(body):
    """
        Registra uma nova movimentação, gerando o próprio código baseado
        no último código registrado no banco.
    """
    ultimo_documento = json.loads(movimentacao_model.Movimentacao.objects.order_by('-codigo').to_json())
    codigo_ultimo_documento = int(ultimo_documento[0]['codigo'])
    codigo = str(codigo_ultimo_documento + 1).zfill(4)
    body['codigo'] = codigo

    return movimentacao_model.Movimentacao(**body).save()


def atualizar_movimentacao(_id, atualizacao):
    movimentacao_model.Movimentacao.objects.get(id=_id).update(**atualizacao)


def deletar_movimentacao(_id):
    movimentacao_model.Movimentacao.objects.get(id=_id).delete()


def movimentacao_queries(body):
    parsed_query_dt = query_parser.parse(body["where"])

    if not "select" in body:
        body["select"] = []

    filted_movimentacao_list = movimentacao_model.Movimentacao.objects(
        __raw__=parsed_query_dt).only(*body["select"])

    return filted_movimentacao_list.to_json()


def deserialize_movimentacao_service(body):
    movimetacao = Movimentacao()

    for att_name, att_value in body.items():
        if "equipamentos_id" is att_name:
            for equipamento in body["equipamentos_id"]:
                movimetacao.equipamentos_id.append(equipamento.id)

        elif "created_at" is att_name:
            movimetacao.created_at = datetime.strptime(body["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

        elif "created_at" is att_name:
            movimetacao.created_at = datetime.strptime(body["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        else:
            try:
                setattr(movimetacao, att_name, att_value)
            except:
                continue

    return movimetacao
    # if "codigo" in body: movimetacao.codigo = body["codigo"]
    # if "tipo" in body: movimetacao.tipo = body["tipo"]
    # if "equipamentos_id" in body:
    #     for equipamento in body["equipamentos_id"]:
    #         movimetacao.equipamentos_id.append(equipamento.id)
    #
    # if "instituicao_destino" in body: movimetacao.instituicao_destino = body["instituicao_destino"]
    # if "cidade_destino" in body: movimetacao.cidade_destino = body["cidade_destino"]
    # if "cnpj_destino" in body: movimetacao.cnpj_destino = body["cnpj_destino"]
    # if "endereco_destino" in body: movimetacao.endereco_destino = body["endereco_destino"]
    # if "nome_responsavel_destino" in body: movimetacao.nome_responsavel_destino = body["nome_responsavel_destino"]
    # if "contato_responsavel_destino" in body: movimetacao.contato_responsavel_destino = body[
    #     "contato_responsavel_destino"]
    # if "nome_responsavel_transporte" in body: movimetacao.nome_responsavel_transporte = body[
    #     "nome_responsavel_transporte"]
    # if "contato_responsavel_transporte" in body: movimetacao.contato_responsavel_transporte = body[
    #     "contato_responsavel_transporte"]
    # if "created_at" in body: movimetacao.created_at = datetime.strptime(body["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
    # if "created_at" in body: movimetacao.updated_at = datetime.strptime(body["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

    #return movimetacao