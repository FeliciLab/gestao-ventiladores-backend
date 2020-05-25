from datetime import datetime
from api.models import ordem_compra_model
from api.utils import query_parser
from api.utils.descerialization_data_model_patch import \
    deserialize_body_to_model


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
        Se a lista de itens for vazia retorna um erro, se não, cria um
        'número_ordem_compra' baseado na quantidade de documentos no banco
         e cadastra uma nova ordem de compra.
    """
    quantidade_itens = len(body['itens'])
    if quantidade_itens == 0:
        return {
            "error": True,
            "message": "Não foram enviados itens suficientes" +
                       "para ordem de compra"
        }

    qtd_ordem_compra = ordem_compra_model.OrdemCompra.objects.count()
    numero_ordem_compra = str(qtd_ordem_compra + 1).zfill(4)
    body['numero_ordem_compra'] = numero_ordem_compra
    return ordem_compra_model.OrdemCompra(**body).save()


def atualizar_ordem_compra(id, atualizacao):
    ordem_compra_model.OrdemCompra.objects \
        .get(id=id).update(itens=atualizacao['itens'])


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
    return deserialize_body_to_model(
        body=body,
        model=ordem_compra_model.OrdemCompra()
    )