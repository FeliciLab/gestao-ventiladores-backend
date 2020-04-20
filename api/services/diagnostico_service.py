from api.models import ordem_servico_model
from api.services import ordem_servico_service


def registar_diagnostico(_id, diagnostico_body):
    ordem_servico_model.OrdemServico.objects.get(id=_id).update(**diagnostico_body)

