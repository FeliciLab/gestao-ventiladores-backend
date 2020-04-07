from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..models import fabricante_model
from ..schemas import fabricante_schema

class FabricanteList(Resource):
    def get(self):
        fabricantes = fabricante_model.Fabricante.objects().to_json()
        return Response(fabricantes, mimetype="application/json", status=200)

    def post(self):
        body = request.json
        fs = fabricante_schema.FabricanteSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            result = fabricante_model.Fabricante(**body).save()
            return make_response(jsonify(result), 201)

class FabricanteDetail(Resource):
    def put(self, fabricante_nome):
        body = request.get_json()
        fabricante_model.Fabricante.objects.get(fabricante_nome=fabricante_nome).update(**body)
        return '', 200

    def delete(self, fabricante_nome):
        fabricante_model.Fabricante.objects.get(fabricante_nome=fabricante_nome).delete()
        return '', 204

    def get(self, fabricante_nome):
        equipamento = fabricante_model.Fabricante.objects.get(fabricante_nome=fabricante_nome).to_json()
        return Response(equipamento, mimetype="application/json", status=200)
