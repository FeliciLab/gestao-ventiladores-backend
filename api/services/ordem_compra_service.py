from api.models import ordem_compra_model
import random

def listar_ordem_compras():
    return ordem_compra_model.OrdemCompra.objects


def listar_ordem_compra_by_id(numero_ordem_compra):
    try:
        return ordem_compra_model.OrdemCompra.objects.get(numero_ordem_compra=numero_ordem_compra)
    except:
        return None


def listar_ordem_compra_by_numero_ordem_compra(numero_ordem_compra):
    try:
        return ordem_compra_model.OrdemCompra.objects.get(numero_ordem_compra=numero_ordem_compra)
    except:
        return None


def registar_ordem_compra(body):
    qtd_ordem_compra = ordem_compra_model.OrdemCompra.objects.count()
    numero_ordem_compra = str(qtd_ordem_compra + 1).zfill(4)
    body['numero_ordem_compra'] = numero_ordem_compra
    return ordem_compra_model.OrdemCompra(**body).save()


