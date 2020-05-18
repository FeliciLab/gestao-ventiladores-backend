from bson.json_util import dumps

from api.models import ordem_servico_model
from api.services import ordem_servico_service
from api.services.ordem_servico_service import \
    get_ordem_servico_equipamento_pipeline


def registar_diagnostico(_id, diagnostico_body):
    ordem_servico_model.OrdemServico.objects.get(id=_id).update(**diagnostico_body)


class DiagnosticService():
    def getDiagnostics(self):
        pipeline = get_ordem_servico_equipamento_pipeline()

        docs = []
        for ordem in ordem_servico_model.OrdemServico \
                .objects(status='diagnostico') \
                .aggregate(pipeline):
            docs.append(ordem)

        return dumps(docs)
