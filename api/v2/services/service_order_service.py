from .service_base import ServiceBase
from ..models.service_order_model import OrdemServico


class ServiceOrderService(ServiceBase):
    def fetch_active(self):
        return self.parser_mongo_response_to_list(
            OrdemServico.objects(deleted_at__exists=False))

    def fetch_all(self):
        return self.parser_mongo_response_to_list(
            OrdemServico.objects())

    def register_service_order(self, body):
        service_order = OrdemServico(**body).save()
        return str(service_order.id)


