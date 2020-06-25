from .service_base import ServiceBase
from ..models.service_order_model import OrdemServico


class ServiceOrderService(ServiceBase):

    def fetch_active(self):
        return self.parser_mongo_response_to_list(
            OrdemServico.objects(deleted_at__exists=False))

    def fetch_all(self):
        return self.parser_mongo_response_to_list(
            OrdemServico.objects())

    def update(self, id):
        pass

    def insert_or_update(self, service_order):
        if '_id' in service_order.keys():
            update(service_order)
        else:
            insert(service_order)

    def insert(self, service_order):
        pass
