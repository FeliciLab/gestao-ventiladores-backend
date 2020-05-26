from datetime import datetime
from api.models import ordem_compra_model
from api.utils import query_parser


def listar_ordem_compras():
    return ordem_compra_model.OrdemCompra.objects


def listar_ordem_compra_by_id(id):
    try:
        return ordem_compra_model.OrdemCompra.objects.get(id=id)
    except Exception:
        return None


def listar_ordem_compra_by_numero_ordem_compra(numero_ordem_compra):
    try:
        return ordem_compra_model.OrdemCompra \
            .objects.get(numero_ordem_compra=numero_ordem_compra)
    except Exception:
        return None


def registar_ordem_compra(body):
    """
        Se a lista de item for vazia retorna um erro, se não, cria um
        'número_ordem_compra' baseado na quantidade de documentos no banco
         e cadastra uma nova ordem de compra.
    """
    quantidade_itens = len(body['item'])
    if quantidade_itens == 0:
        return {
            "error": True,
            "message": "Não foram enviados item suficientes" +
                       "para ordem de compra"
        }

    qtd_ordem_compra = ordem_compra_model.OrdemCompra.objects.count()
    numero_ordem_compra = str(qtd_ordem_compra + 1).zfill(4)
    body['numero_ordem_compra'] = numero_ordem_compra
    return ordem_compra_model.OrdemCompra(**body).save()


def atualizar_ordem_compra(id, atualizacao):
    ordem_compra_model.OrdemCompra.objects \
        .get(id=id).update(itens=atualizacao['item'])


def deletar_ordem_compra(_id):
    ordem_compra_model.OrdemCompra.objectsget(id=_id).delete()


def ordem_compra_queries(body):

    parsed_query_dt = query_parser.parse(body["where"])

    if "select" not in body:
        body["select"] = []

    filted_ordem_compra_list = ordem_compra_model.OrdemCompra \
        .objects(__raw__=parsed_query_dt).only(*body["select"])

    return filted_ordem_compra_list.to_json()


def deserealize_ordem_compra(body):
    ordem_compra = ordem_compra_model.OrdemCompra()

    for att_name, att_value in body.items():

        if "created_at" == att_name:
            ordem_compra.created_at = datetime \
                .strptime(body["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

        if "created_at" == att_name:
            ordem_compra.created_at = datetime \
                .strptime(body["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        else:
            try:
                setattr(ordem_compra, att_name, att_value)
            except Exception:
                continue

    return ordem_compra
