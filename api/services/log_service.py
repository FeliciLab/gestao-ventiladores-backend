from ..models import log_model
from ..services import ordem_servico_service, ordem_compra_service, equipamento_service
from datetime import datetime
import json


def log_criacao(collection, objeto_criado):
    values = json.loads(objeto_criado.to_json())
    values['id'] = values['_id']
    log_model.Log(collection=collection,
                  document_id=objeto_criado.id,
                  old_values=values,
                  last_updated_at=datetime.now(),
                  created_at=datetime.now()).save()

def log_atualizacao_ordem_compra(collection, id, body):
    ordem_compra = json.loads(ordem_compra_service.listar_ordem_compra_by_id(id).to_json())
    log = {}
    for k, v in body.items():
        if k in ordem_compra:
            log[k] = v

    log_model.Log(collection=collection,
                  document_id=id,
                  old_values=log,
                  last_updated_at=datetime.now(),
                  created_at=datetime.now()).save()

def log_atualizacao_equipamento(collection, id, body):
    equipamento = json.loads(equipamento_service.listar_equipamento_by_id(id).to_json())
    log = {}
    for k, v in body.items():
        if k in equipamento:
            if equipamento[k] != v:
                log[k] = v

    log_model.Log(collection=collection,
                  document_id=id,
                  old_values=log,
                  last_updated_at=datetime.now(),
                  created_at=datetime.now()).save()


def log_atualizacao_ordem_servico(collection, id, body):
    ordem_servico = json.loads(ordem_servico_service.listar_ordem_servico_by_id(id).to_json())
    log = {}
    for k, v in body.items():
        if k == 'triagem':
            for k_triagem, v_triagem in body['triagem']:
                if k_triagem in ordem_servico['triagem']:
                    log['triagem'][k_triagem] = v_triagem
        if k == 'diagnostico':
            for k_diagnostico, v_diagnostico in body['diagnostico']:
                if k_diagnostico in ordem_servico['diagnostico']:
                    log['diagnostico'][k_diagnostico] = v_diagnostico

        if k in ordem_servico:
            log[k] = v

    log_model.Log(collection=collection,
                  document_id=id,
                  old_values=log,
                  last_updated_at=datetime.now(),
                  created_at=datetime.now()).save()