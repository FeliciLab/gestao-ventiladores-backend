from api.models import fabricante_model


def listar_fabricantes():
    return fabricante_model.Fabricante.objects.to_json()


def listar_fabricante_id(fabricante_nome):
    try:
        fabricante = fabricante_model.Fabricante.objects.get(id=fabricante_nome).to_json()
    except:
        fabricante = None
    finally:
        return fabricante


def registar_fabricante(body):
    return fabricante_model.Fabricante(**body).save().to_json()


def atualizar_fabricante(fabricante_nome, atualizacao):
    fabricante_model.Fabricante.objects.get(id=fabricante_nome).update(**atualizacao)


def deletar_fabricante(fabricante_nome):
    fabricante_model.Fabricante.objects.get(id=fabricante_nome).delete()
