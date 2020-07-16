from api.v2.models.equipamento_model import Equipamento
from api.v2.models.item_model import Item


def get_pipeline_join(join):
    pipeline = []
    if "equipamento" in join:
        pipeline.append({
            "$lookup": {
                "from": Equipamento._get_collection_name(),
                "localField": "equipamento_id",
                "foreignField": "_id",
                "as": "equipamento"
            }
        })

    if "item" in join:
        pipeline.append({
            '$lookup': {
                'from': Item._get_collection_name(),
                'localField': 'triagem.acessorios.item_id',
                'foreignField': '_id',
                'as': 'itens'
            }
        })

        pipeline.append({
            '$lookup': {
                'from': Item._get_collection_name(),
                'localField': 'diagnostico.itens.item_id',
                'foreignField': '_id',
                'as': 'itens'
            }
        })

    return pipeline
