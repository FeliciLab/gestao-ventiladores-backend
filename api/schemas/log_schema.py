from ..models import log_model
from marshmallow import Schema, fields


class LogSchema(Schema):
    class Meta:
        model = log_model.Log
        fields = ("collection", "document_id", "old_values", "user", "last_updated_at", "created_at")

    collection = fields.String(required=True)
    document_id = fields.String(required=False)
    old_values = fields.String(required=False)
    user = fields.String(required=False)
    last_updated_at = fields.DateTime(required=False)
    created_at = fields.DateTime(required=False)