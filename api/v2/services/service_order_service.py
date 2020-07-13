from .service_base import ServiceBase
from ..models.service_order_model import OrdemServico
from ..utils.util_update import update_only_fields
from api.v2.utils.service_order_utils import get_pipeline_join


class ServiceOrderService(ServiceBase):
    def fetch_all(self, join=None, deleted=None):
        deleted = deleted == True
        if join:
            query = OrdemServico.objects(
                status__ne='tmp',
                deleted_at__exists=deleted
            ).aggregate(get_pipeline_join(join))
        else:
            query = OrdemServico.objects(
                status__ne='tmp',
                deleted_at__exists=deleted
            )

        return self.parser_mongo_response_to_list(
            self.parse_query_aggregate_to_list(query_result=query)
        )

    def fetch_active(self, join):
        return self.fetch_all(join=join, deleted=False)

    def fetch_service_order_by_id(self, _id):
        return OrdemServico.objects(id=_id).first()

    def update(self, id, service_order):
        update_only_fields(_id=id, data=service_order, model=OrdemServico)

    def insert_or_update(self, service_order):
        if "_id" in service_order.keys():
            self.update(service_order)
        else:
            self.insert(service_order)

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
