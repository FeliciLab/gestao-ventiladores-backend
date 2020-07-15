from ..models.service_order_model import OrdemServico


def fetch_all():
    return OrdemServico.objects()
