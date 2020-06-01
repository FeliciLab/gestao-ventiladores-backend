from ..models.item_model import Item
from .service_base import ServiceBase


class ItemService(ServiceBase):
    def fetch_items_list(self, deleted=False):
        if deleted:
            return self.parser_mongo_response_to_list(
                Item.objects())
        
        return self.parser_mongo_response_to_list(
            Item.objects(deleted_at__exists=False))


    def fetch_item_by_id(self, _id):
        return Item.objects(id=_id).first()
