from ..models.item_model import Item
from .service_base import ServiceBase
from ..helpers.helper_update import define_updated_fields, update_only_fields


class ItemService(ServiceBase):
    def fetch_items_list(self, deleted=False):
        if deleted:
            return self.parser_mongo_response_to_list(
                Item.objects())

        return self.parser_mongo_response_to_list(
            Item.objects(deleted_at__exists=False))

    def fetch_item_by_id(self, _id):
        return Item.objects(id=_id).first()

    def register_item(self, body):
        item = Item(**body).save()
        return str(item.id)

    def update_item_only_fields(self, data, id):
        update_only_fields(_id=id, data=data, model=Item)
