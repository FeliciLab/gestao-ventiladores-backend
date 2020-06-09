

def invalid_deleted_parameter(param):
    return param and param != "true"

def validate_post(body):
    if '_id' in body: 
        return (False, 'ID must not be sent')
    return (True, 'OK')

def validate_request(body):
    if not body:
        return (False, 'No body found')

    if not isinstance(body['content'], list):
        return (False, 'No list found.')

    if not len(body['content']):
        return (False, 'Empty list. Nothing to do.')
    
    for item in body['content']:
        if not item: 
            return (False, 'Some entry has no data to insert.')

    return (True, 'OK')
