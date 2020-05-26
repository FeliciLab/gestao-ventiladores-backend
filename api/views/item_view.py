from flask_restful import Resource
from flasgger import swag_from

class ItemMany(Resource):
    @swag_from('../../documentacao/item/item_get_many.yml')
    def get(self):
        pass


    @swag_from('../../documentacao/item/item_post_many.yml')
    def post(self):
        pass


    @swag_from('../../documentacao/item/item_put_many.yml')
    def put(self):
        pass


    @swag_from('../../documentacao/item/item_patch_many.yml')
    def patch(self):
        pass


    @swag_from('../../documentacao/item/item_delete_many.yml')
    def delete(self):
        pass


class ItemOne(Resource):
    @swag_from('../../documentacao/item/item_get_one.yml')
    def get(self, _id):
        pass


    @swag_from('../../documentacao/item/item_put_one.yml')
    def put(self, _id):
        pass


    @swag_from('../../documentacao/item/item_patch_one.yml')
    def patch(self):
        pass


    @swag_from('../../documentacao/item/item_delete_one.yml')
    def delete(self, _id):
        pass


class ItemFind(Resource):
    @swag_from('../../documentacao/item/item_find.yml')
    def post(self):
        pass
