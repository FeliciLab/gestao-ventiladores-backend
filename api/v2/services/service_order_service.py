from .service_base import ServiceBase
from ..models.service_order_model import OrdemServico


class ServiceOrderService(ServiceBase):
    def fetch_active(self):
        return self.parser_mongo_response_to_list(
            OrdemServico.objects(deleted_at__exists=False)
        )

    def fetch_all(self):
        return self.parser_mongo_response_to_list(OrdemServico.objects())

    def fetch_service_order_by_id(self):
        return OrdemServico.objects(id=_id).first()

    def update(self, id):
        pass

    def insert_or_update(self, service_order):
        if "_id" in service_order.keys():
            update(service_order)
        else:
            insert(service_order)

    def insert(self, service_order):
        pass
        return self.parser_mongo_response_to_list(OrdemServico.objects())

    def save_service_order(self, service_order):
        service_order = OrdemServico(**service_order).save()
        return str(service_order.id)

    def format_service_order_number(self, service_order_number):
        return str(service_order_number).zfill(4)

    def check_duplicates_service_order_number(self, service_order_number):
        return OrdemServico.objects(numero_ordem_servico=service_order_number)
