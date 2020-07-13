def pop_id(data):
    id = data['_id']
    try:
        del data['_id']
    except Exception:
        return Exception

    return id


def define_updated_fields(current_key, current_value):
    """
    current_key: String
    current_value: Any Primitive type
    """
    query = {}
    if type(current_value) == dict:
        for k, v in current_value.items():
            query.update(define_updated_fields(
                current_key + "__{}".format(k), v))

    else:
        query[current_key] = current_value
    return query


def update_only_fields(_id, data, model):
    """
    _id: ObjectId
    data: Dict
    model: Mongoengine.Document
    """
    query = {}
    root_key = "set"
    root_value = data
    query.update(define_updated_fields(root_key, root_value))

    model.objects(id=_id).update(**query)
