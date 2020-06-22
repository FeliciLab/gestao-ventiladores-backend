from marshmallow import ValidationError


class SchemaBase():
    def validate_posts(self, item):
        if '_id' in item:
            return False, 'Id must not be sent'

        if 'updated_at' in item:
            return False, 'Updated must not be sent'

        if 'deleted_at' in item:
            return False, 'Deleted must not be sent'

        try:
            self.load(item)
        except ValidationError as err:
            return False, err.messages

        return True, 'OK'
