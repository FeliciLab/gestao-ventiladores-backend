from marshmallow import Schema, fields

from api.models import movimentacao_model


class MovimentacaoSchema(Schema):
    class Meta:
        model = movimentacao_model.Movimentacao
        fields = (
            "_id",
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

    tipo = fields.String(required=False)
    tipo = fields.String(required=False)
    #equipamento_id = fields.String(required=True) todo a gente nao sabe como ficaria
    instituicao_destino = fields.String(required=False)
    cidade_destino = fields.String(required=False)
    cnpj_destino = fields.String(required=False)
    endereco_destino = fields.String(required=False)
    nome_responsavel_destino = fields.String(required=False)
    contato_responsavel_destino = fields.String(required=False)
    nome_responsavel_transport = fields.String(required=False)
    contato_responsavel_transport = fields.String(required=False)
