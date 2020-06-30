from http import HTTPStatus
from flask import request
from .dtos.service_order_request import ServiceOrderRequest
from flask_restful import Resource
from ..helpers.helper_response import get_response
from ..validation.validation_request import invalid_deleted_parameter
from api.v2.controllers.validators.validation_request import (
    validate_request,
    validate_request_id,
    validate_request_dict_id,
)
from api.v2.services.service_order_service import ServiceOrderService
from api.v2.models.schemas.service_order_schema import ServiceOrderSchema
from api.v2.utils.util_response import error_response, post_response
from ..utils.util_update import pop_id


class ServiceOrdersManyController(Resource):
    def get(self):
        deleted_included = request.args.get("deleted")
        if invalid_deleted_parameter(deleted_included):
            return error_response(
                "Parameter deleted is not equal true.", HTTPStatus.BAD_REQUEST
            )
        if deleted_included:
            service_orders = ServiceOrderService().fetch_all()
        else:
            service_orders = ServiceOrderService().fetch_active()

        return get_response(service_orders, deleted_included)

    def patch(self):
        body = request.get_json()
        validate, message = validate_request(body)
        if not validate:
            return error_response(message)

        errors = []
        for index, service_order in enumerate(body["content"]):
            validate, message = ServiceOrderSchema().validate_updates(
                service_order, index
            )

            if not validate:
                errors.append({index: message})

            validate, message = validate_request_dict_id("service_order", service_order)
            if not validate:
                errors.append({index: message})

        if errors:
            return error_response(errors)

        for index, service_order in enumerate(body["content"]):
            id = pop_id(service_order)
            ServiceOrderService().update(id, service_order)

        return "", 200

    def post(self):
        body = request.get_json()

        validate, message = validate_request(body)
        if not validate:
            return error_response(message)

        errors = []
        for index, service_order in enumerate(body["content"]):
            validate, message = ServiceOrderSchema().validate_save(service_order)
            if not validate:
                errors.append({index: message})
                continue

            validate, message = validate_request_id(
                "equipamento", service_order["equipamento_id"]
            )
            if not validate:
                errors.append({index: message})

            accessories = service_order["triagem"]["acessorios"]
            for accessory in accessories:
                validate, message = validate_request_id("item", accessory["item_id"])
                if not validate:
                    errors.append({index: message})

            items = service_order["diagnostico"]["itens"]
            for item in items:
                validate, message = validate_request_id("item", item["item_id"])
                if not validate:
                    errors.append({index: message})

            service_order[
                "numero_ordem_servico"
            ] = ServiceOrderService().format_service_order_number(
                service_order["numero_ordem_servico"]
            )

            if ServiceOrderService().check_duplicates_service_order_number(
                service_order["numero_ordem_servico"]
            ):
                errors.append({index: "Service Order number already exists"})

        if errors:
            return error_response(errors)

        content = []
        for service_order in body["content"]:
            content.append(ServiceOrderService().save_service_order(service_order))

        return post_response(content)
