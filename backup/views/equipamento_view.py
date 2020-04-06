from flask import Response, request
from models.triagem_modelo import Equipamento
from flask_restful import Resource


# Modelo sem parâmetro
class EquipamentoList(Resource):
    def get(self):
        equipamentos = Equipamento.objects().to_json()
        return Response(equipamentos, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        equipamento = Equipamento(**body).save()
        numero_ordem_servico = equipamento.numero_ordem_servico # aqui é esse id  ou mesmo o numero_ordem_servico ? eu acho
        return {'numero_ordem_servico': numero_ordem_servico}, 201


# Modelo com parâmetro
class EquipamentoDetail(Resource):
    def put(self, numero_ordem_servico):
        body = request.get_json()
        Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico).update(**body) # aqui é esse id  ou mesmo o numero_ordem_servico ? eu acho
        return '', 200

    def delete(self, numero_ordem_servico):
        movie = Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico).delete() # aqui é esse id  ou mesmo o numero_ordem_servico ? eu acho
        return '', 200

    def get(self, numero_ordem_servico):
        movies = Equipamento.objects.get(numero_ordem_servico=numero_ordem_servico).to_json() # aqui é esse id  ou mesmo o numero_ordem_servico ? eu acho
        return Response(movies, mimetype="application/json", status=200)