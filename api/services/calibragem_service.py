from bson.json_util import dumps

from api.models import ordem_servico_model
from api.services.ordem_servico_service import \
    get_ordem_servico_equipamento_pipeline


class CalibragemService:
    def getCalibrations(self):
        pipeline = get_ordem_servico_equipamento_pipeline()

        docs = []
        for ordem in ordem_servico_model.OrdemServico \
                .objects(status='calibragem') \
                .aggregate(pipeline):
            docs.append(ordem)

        return dumps(docs)

    def update_order_service_calibration(self, _id, doc):
        prefix = 'set__calibragem__{}'
        query = {}

        if 'status' in doc:
            query['set__status'] = doc['status']

        if 'status' in doc['calibragem']:
            query[prefix.format('status')] = doc['calibragem']['status']

        return ordem_servico_model.OrdemServico \
            .objects(id=_id) \
            .update(**query)
