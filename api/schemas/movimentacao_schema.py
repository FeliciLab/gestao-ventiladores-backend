from flask_restful import fields
from marshmallow import Schema

from api.models import movimentacao_model


class MovimentacaoSchema(Schema):
    class Meta:
        model = movimentacao_model.Movimentacao
        fields = (
            "tipo",
            "equipamento_id",
            "instituicao_destino",
            "cidade_destino",
            "cnpj_destino",
            "endereco_destino",
            "nome_responsavel_destino",
            "contato_responsavel_destino",
            "nome_responsavel_transport",
            "contato_responsavel_transport"

        )

    tipo = fields.String(required=True)
    #equipamento_id = fields.String(required=True) todo a gente nao sabe como ficaria
    instituicao_destino = fields.String(required=True)
    cidade_destino = fields.String(required=True)
    cnpj_destino = fields.String(required=True)
    endereco_destino = fields.String(required=True)
    nome_responsavel_destino = fields.String(required=True)
    contato_responsavel_destino = fields.String(required=True)
    nome_responsavel_transport = fields.String(required=True)
    contato_responsavel_transport = fields.String(required=True)
