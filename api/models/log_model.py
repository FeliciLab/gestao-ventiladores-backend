from config.db import db
from datetime import datetime


class Log(db.Document):
    collection = db.StringField(required=True)
    document_id = db.ObjectIdField(required=False)
    old_values = db.DictField(required=False)
    user = db.StringField(required=False)
    last_updated_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
