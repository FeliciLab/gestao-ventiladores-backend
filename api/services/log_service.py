from ..models import log_model
from ..services import ordem_servico_service, ordem_compra_service, equipamento_service, movimentacao_service
from datetime import datetime
import json


def log_atualizacao_ordem_compra(collection, id, body):
    ordem_compra = json.loads(ordem_compra_service.listar_ordem_compra_by_id(id).to_json())
    log = {}
    for key, value in body.items():
        if key in ordem_compra:
            log[key] = value


    if len(log) == 0:
        pass
    else:
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

    if len(log) == 0:
        pass
    else:
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
            log['triagem'] = {}
            for k_triagem, v_triagem in body['triagem'].items():
                if k_triagem in ordem_servico['triagem']:
                    log['triagem'][k_triagem] = v_triagem
        if k == 'diagnostico':
            for k_diagnostico, v_diagnostico in body['diagnostico'].items():
                if k_diagnostico in ordem_servico['diagnostico']:
                    log['diagnostico'] = {}
                    log['diagnostico'][k_diagnostico] = v_diagnostico

        if k in ordem_servico:
            log[k] = v

    if len(log) == 0:
        pass
    else:
        log_model.Log(collection=collection,
                      document_id=id,
                      old_values=log,
                      last_updated_at=datetime.now(),
                      created_at=datetime.now()).save()

def log_atualizacao_movimentacao(collection, id, body):
    movimentacao = json.loads(movimentacao_service.listar_movimentacao_id(id).to_json())
    log = {}
    for k, v in body.items():
        if k in movimentacao:
            if movimentacao[k] != v:
                log[k] = v

    if len(log) == 0:
        pass
    else:
        log_model.Log(collection=collection,
                      document_id=id,
                      old_values=log,
                      last_updated_at=datetime.now(),
                      created_at=datetime.now()).save()