from .service_base import ServiceBase
from ..models.service_order_model import OrdemServico


class ServiceOrderService(ServiceBase):
   def fetch_all(self):
        return self.parser_mongo_response_to_list(
            OrdemServico.objects())
