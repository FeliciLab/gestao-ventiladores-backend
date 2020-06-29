from marshmallow import ValidationError


class SchemaBase:
    def validate_save(self, body):
        if "_id" in body:
            return False, "Id must not be sent"

        if "updated_at" in body:
            return False, "Updated must not be sent"

        if "deleted_at" in body:
            return False, "Deleted must not be sent"

        try:
            self.load(body)
        except ValidationError as err:
            return False, err.messages

        return True, "OK"

    def validate_updates(self, entity: dict, index: int, fields: tuple):
        try:
            self.load(entity, partial=fields)
        except ValidationError as err:
            return {index: err.messages}
