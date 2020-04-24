from api.models import movimentacao_model
from api.utils import query_parser


def listar_movimentacoes():
    return movimentacao_model.Movimentacao.objects()


def listar_movimentacao_id(_id):
    try:
        movimentacao = movimentacao_model.Movimentacao.objects.get(id=_id)
    except:
        movimentacao = None
    finally:
        return movimentacao


def registar_movimentacao(body):
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
