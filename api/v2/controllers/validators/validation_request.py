from bson import ObjectId
from api.v2.services.item_service import ItemService
from api.services.equipamento_service import listar_equipamento_by_id
from ...services.service_order_service import ServiceOrderService
from ...validation.schemas.item_schema import ItemSchema
from ...helpers.helper_response import error_response


def invalid_deleted_parameter(param):
    return param and param != "true"


def validate_is_list(body):
    if isinstance(type(body), list):
        return (False, "Not a list.")
    return (True, "OK")


def validate_post(body):
    if "_id" in body:
        return (False, "ID must not be sent")
    return (True, "OK")


def validate_request(body):
    if not body:
        return (False, "No body found")

    if not "content" in body:
        return (False, "No content found")

    if not isinstance(body["content"], list):
        return (False, "No list found.")

    if not len(body["content"]):
        return (False, "Empty list. Nothing to do.")

    for item in body["content"]:
        if not item:
            return (False, "Some entry has no data.")

    return (True, "OK")


def validate_id_included(entity):
    if "_id" not in entity:
        return (False, "Missing ID")
    return (True, "OK")


def validate_id_objectID(_id):
    try:
        ObjectId(_id)
    except Exception:
        return (False, "Invalid ID")
    return (True, "OK")


def validate_id_exists(entity, _id):
    if entity == "item":
        if not ItemService().fetch_item_by_id(_id):
            return (False, "Nonexistent item ID")

    if entity == "equipamento":
        if not listar_equipamento_by_id(_id):
            return (False, "Nonexistent equipamento ID")

    if entity == "service_order":
        if not ServiceOrderService().fetch_service_order_by_id(_id):
            return (False, "Nonexistent service order ID")

    return (True, "OK")


def validate_request_dict_id(name_entity: str, entity: dict):
    validate, message = validate_id_included(entity)
    if not validate:
        return (validate, message)

    validate, message = validate_request_id(name_entity, entity["_id"])
    if not validate:
        return (validate, message)

    return (True, "OK")


def validate_request_id(name_entity: str, _id: str):
    validate, message = validate_id_objectID(_id)
    if not validate:
        return validate, message

    validate, message = validate_id_exists(name_entity, _id)
    if not validate:
        return validate, message

    return (True, "OK")


def validate_merge_items_request(body):
    if "content" not in body:
        return False, "Wrong format."

    if "toUpdate" not in body["content"]:
        return False, "Request without field toUpdate."

    if "toRemove" not in body["content"]:
        return False, "Request without field toRemove."

    if not bool(body["content"]["toUpdate"]):
        return False, "Field toUpdate can't be empty object."

    if not bool(body["content"]["toRemove"]):
        return False, "Field toRemove can't be empty list."

    errors = {}

    errors_toUpdate = ItemSchema().validate(body["content"]["toUpdate"])
    if errors_toUpdate:
        errors["toUpdate"] = errors_toUpdate

    errors_toRemove = {}
    for index, item in enumerate(body["content"]["toRemove"]):
        erro_schema = ItemSchema().validate(item)
        if erro_schema:
            errors_toRemove[str(index)] = erro_schema
    if errors_toRemove:
        errors["toRemove"] = errors_toRemove

    if errors:
        return False, errors

    return True, ""
