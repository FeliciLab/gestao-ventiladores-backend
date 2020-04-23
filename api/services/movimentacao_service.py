from api.models import movimentacao_model


def listar_movimentacoes():
    return movimentacao_model.Movimentacao.objects


def listar_fmovimentacao_id(_id):
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
