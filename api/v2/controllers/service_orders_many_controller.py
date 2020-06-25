from http import HTTPStatus
from flask import request
from flask_restful import Resource
from ..helpers.helper_response import get_response
from ..validation.validation_request import invalid_deleted_parameter
from api.v2.controllers.validators.validation_request import validate_request
from api.v2.services.service_order_service import ServiceOrderService
from api.v2.models.schemas.service_order_schema import ServiceOrderSchema
from api.v2.utils.util_response import error_response, post_response
from .validators.validation_request import validate_request_id


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

    def post(self):
        body = request.get_json()

        validate, message = validate_request(body)
        if not validate:
            return error_response(message)

        errors = []
        for index, service_order in enumerate(body["content"]):
            validate, message = ServiceOrderSchema().validate_post(service_order)
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

            service_order["numero_ordem_servico"] = ServiceOrderService().create_service_order_number(
                service_order["numero_ordem_servico"]
            )

            if ServiceOrderService().check_duplicates_service_order_number(service_order["numero_ordem_servico"]):
                errors.append({index: 'Service Order number already exists'})

        if errors:
            return error_response(errors)

        content = []
        for service_order in body["content"]:
            content.append(ServiceOrderService().register_service_order(service_order))

        return post_response(content)

    # this method is here for pr review purposes only 
    def alternative_post(self):

        service_order_request = ServiceOrderRequest(request)
        
        service_order = ServiceOrderService().save(service_order_request)

        return ServiceOrderResponse(service_order)
