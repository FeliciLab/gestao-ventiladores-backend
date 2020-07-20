import json


def parser_mongo_response_to_list(mongo_response):
    docs = []
    for obj in mongo_response:
        obj = convert_mongo_to_dict(obj)
        remove_oid(obj)
        remove_date(obj)
        docs.append(obj)

    return docs


def convert_mongo_to_dict(obj):
    return json.loads(obj.to_json())


def remove_oid(obj):
    for key, value in obj.items():
        if isinstance(value, dict):
            remove_oid(value)

        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    remove_oid(item)

        if key == '_id':
            obj['_id'] = obj['_id']['$oid']

        if key == 'equipamento_id':
            obj['equipamento_id'] = obj['equipamento_id']['$oid']

        if key == 'item_id':
            obj['item_id'] = obj['item_id']['$oid']


def remove_date(obj):
    for key, value in obj.items():
        if isinstance(value, dict):
            remove_date(value)

        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    remove_date(item)

        if key == 'created_at':
            obj['created_at'] = obj['created_at']['$date']

        if key == 'updated_at':
            obj['updated_at'] = obj['updated_at']['$date']

        if key == 'deleted_at' and obj['deleted_at']:
            obj['deleted_at'] = obj['deleted_at']['$date']
