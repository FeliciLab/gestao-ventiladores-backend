from ..models.item_model import Item


class ItemService():
    def list_items(self, deleted=False):
        if deleted:
            return Item.objects()
        
        return Item.objects(deleted_at__exists=False)


    def list_item_by_id(self, _id):
        return Item.objects(id=_id).first()
