import json
from flask import Response, request, jsonify
from flask_restful import Resource
from api.schemas import ordem_servico_schema
from api.services.calibragem_service import CalibragemService
from api.utils.error_response import error_response


class CalibragemCrud(Resource):
    def get(self):
        ordem_servicos_calibrados = CalibragemService().getCalibrations()
        return Response(ordem_servicos_calibrados, mimetype="application/json",
                        status=200)

    def post(self):
        body = request.json
        _id = body['_id'] if '_id' in body else False
        if not _id:
            return error_response('ID não enviado')

        if 'calibragem' not in body:
            return error_response('Calibragem não enviada.')

        error_validacao = ordem_servico_schema \
            .CalibragemSchema() \
            .validate(body['calibragem'])

        if error_validacao:
            return jsonify(error_validacao)

        CalibragemService().update_order_service_calibration(_id=_id, doc=body)

        return Response(
            json.dumps({'_id': _id}),
            mimetype='application/json',
            status=200 if _id else 201
        )

    def put(self):
        pass
