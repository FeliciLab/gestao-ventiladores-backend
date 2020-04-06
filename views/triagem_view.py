from flask import Response, request

from flask_restful import Resource


# Modelo sem parâmetro
from models.triagem_modelo import Triagem


class TriagemList(Resource):
    def get(self):
        equipamentos = Triagem.objects().to_json()
        return Response(equipamentos, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        equipamento = Triagem(**body).save()
        numero_ordem_servico = equipamento.numero_ordem_servico # aqui é esse id  ou mesmo o numero_ordem_servico ? eu acho
        return {'numero_ordem_servico': numero_ordem_servico}, 201


# Modelo com parâmetro
class TriagemDetail(Resource):
    def put(self, id):
        body = request.get_json()
        print(body)
        Triagem.objects.get(numero_ordem_servico=id).update(**body) # aqui é esse id  ou mesmo o numero_ordem_servico ? eu acho
        return '', 200

    def delete(self, id):
        Triagem.objects.get(numero_ordem_servico=id).delete() # aqui é esse id  ou mesmo o numero_ordem_servico ? eu acho
        return '', 200

    def get(self, id):
        movies = Triagem.objects.get(numero_ordem_servico=id).to_json() # aqui é esse id  ou mesmo o numero_ordem_servico ? eu acho
        return Response(movies, mimetype="application/json", status=200)