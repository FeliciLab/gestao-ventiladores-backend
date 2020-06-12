from bson import ObjectId
from ..services.item_service import ItemService


def invalid_deleted_parameter(param):
    return param and param != "true"


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
            return (False, 'Some entry has no data to insert.')

    return (True, 'OK')


def validate_id(entity):
    if '_id' not in entity:
        return (False, 'Missing ID')

    try:
        ObjectId(entity['_id'])
    except Exception:
        return (False, 'Invalid ID')

    if not ItemService().fetch_item_by_id(entity['_id']):
        return (False, 'Nonexistent ID')

    return (True, 'OK')
