import json
from bson.json_util import dumps

class ServiceBase():
    def parse_query_aggregate_to_list(self, query_result):
        docs = []
        for data in query_result:
            docs.append(data)

        return docs

    def parser_mongo_response_to_list(self, mongo_response):
        docs = []
        for obj in mongo_response:
            obj = self.convert_mongo_to_dict(obj) if type(obj) is not dict else json.loads(dumps(obj))
            print(obj)
            self.remove_oid(obj)
            self.remove_date(obj)
            docs.append(obj)

        return docs

    def convert_mongo_to_dict(self, obj):

        return json.loads(obj.to_json())

    def remove_oid(self, obj):
        for key, value in obj.items():
            if isinstance(value, dict):
                self.remove_oid(value)

            if isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self.remove_oid(item)

            if key == '_id':
                obj['_id'] = obj['_id']['$oid']

            if key == 'equipamento_id':
                obj['equipamento_id'] = obj['equipamento_id']['$oid']

            if key == 'item_id':
                obj['item_id'] = obj['item_id']['$oid']

    def remove_date(self, obj):
        for key, value in obj.items():
            if isinstance(value, dict):
                self.remove_date(value)

            if isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self.remove_date(item)  

            if key == 'created_at':
                obj['created_at'] = obj['created_at']['$date']
            
            if key == 'updated_at':
                obj['updated_at'] = obj['updated_at']['$date']

            if key == 'deleted_at' and obj['deleted_at']:
                obj['deleted_at'] = obj['deleted_at']['$date']


