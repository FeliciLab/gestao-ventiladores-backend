from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..models import equipamento_model
from ..schemas import equipamento_schema

class EquipamentoList(Resource):
    def get(self):
        equipamentos = equipamento_model.Equipamento.objects().to_json()
        return Response(equipamentos, mimetype="application/json", status=200)

    def post(self):
        body = request.json
        es = equipamento_schema.EquipamentoSchema()
        validate = es.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            result = equipamento_model.Equipamento(**body).save()
            return make_response(jsonify(result), 201)

class EquipamentoDetail(Resource):
    def put(self, numero_ordem_servico):
        body = request.get_json()
        equipamento_model.Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico).update(**body) # aqui é esse id  ou mesmo o numero_ordem_servico ? eu acho
        return '', 200

    def delete(self, numero_ordem_servico):
        equipamento_model.Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico).delete() # aqui é esse id  ou mesmo o numero_ordem_servico ? eu acho
        return '', 200

    def get(self, numero_ordem_servico):
        equipamento = equipamento_model.Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico).to_json() # aqui é esse id  ou mesmo o numero_ordem_servico ? eu acho
        return Response(equipamento, mimetype="application/json", status=200)
