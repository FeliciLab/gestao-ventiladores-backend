from api.models import ordem_compra
import random

def listar_ordem_compras():
    return ordem_compra.OrdemCompra.objects


def listar_ordem_compra_by_id(numero_ordem_compra):
    try:
        return ordem_compra.OrdemCompra.objects.get(numero_ordem_compra=numero_ordem_compra)
    except:
        return None


def listar_ordem_compra_by_numero_ordem_compra(numero_ordem_compra):
    try:
        return ordem_compra.OrdemCompra.objects.get(numero_ordem_compra=numero_ordem_compra)
    except:
        return None


def registar_ordem_compra(body):
    print(body)
    body["numero_ordem_compra"] = random.getrandbits(128)
    return ordem_compra.OrdemCompra(**body).save()


