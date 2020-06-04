import json


class ServiceBase():
    def parser_mongo_response_to_list(self, mongo_response):
        docs = []
        for obj in mongo_response:
            obj = self.convert_mongo_to_dict(obj)
            self.remove_oid(obj)
            self.remove_date(obj)
            docs.append(obj)

        return docs

    def convert_mongo_to_dict(self, obj):
        return json.loads(obj.to_json())

    def remove_oid(self, obj):
        if '_id' in obj:
            obj['_id'] = obj['_id']['$oid']

    def remove_date(self, obj):
        if 'created_at' in obj:
            obj['created_at'] = obj['created_at']['$date']

        if 'updated_at' in obj:
            obj['updated_at'] = obj['updated_at']['$date']

        if 'deleted_at' in obj:
            obj['deleted_at'] = obj['deleted_at']['$date']
