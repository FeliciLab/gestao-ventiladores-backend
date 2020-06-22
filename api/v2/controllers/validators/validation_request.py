from bson import ObjectId


def invalid_deleted_parameter(param):
    return param and param != "true"


def validate_is_list(body):
    if isinstance(type(body), list):
        return (False, 'Wrong format.')
    return (True, 'OK')


def validate_exists_id(id, service):
    try:
        ObjectId(id)
    except Exception:
        return (False, 'Invalid ID')

    if not service.fetch_item_by_id(id):
        return (False, 'Nonexistent ID')

    return (True, 'OK')


def validate_post(body):
    if '_id' in body:
        return (False, 'ID must not be sent')
    return (True, 'OK')


def validate_request(body):
    if not body:
        return (False, 'No body found')

    if not 'content' in body:
        return (False, 'No content found')

    if not isinstance(body['content'], list):
        return (False, 'No list found.')

    if not len(body['content']):
        return (False, 'Empty list. Nothing to do.')
    for item in body['content']:
        if not item:
            return (False, 'Some entry has no data.')

    return (True, 'OK')


def validate_id_included(entity):
    if '_id' not in entity:
        return (False, 'Missing ID')
    return (True, 'OK')


def validate_id_objectID(_id):
    try:
        ObjectId(_id)
    except Exception:
        return (False, 'Invalid ID')
    return (True, 'OK')


def validate_item_id_exists(_id, service):
    if not service.fetch_item_by_id(_id):
        return (False, 'Nonexistent ID')
    return (True, 'OK')


def validate_request_dict_id(entity):
    validate, message = validate_id_included(entity)
    if not validate:
        return (validate, message)

    validate, message = validate_request_id(entity['_id'])    
    if not validate:
        return (validate, message)       
    
    return (True, 'OK')


def validate_request_id(_id):
    validate, message = validate_id_objectID(_id)
    if not validate:
        return (validate, message)

    validate, message = validate_item_id_exists(_id)
    if not validate:
        return (validate, message)

    return (True, 'OK')
