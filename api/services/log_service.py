from bson import ObjectId

from ..models import log_model
from ..services import ordem_servico_service, ordem_compra_service, equipamento_service, movimentacao_service
from datetime import datetime
import json
from ..utils import query_parser


# def log_atualizacao_ordem_compra(collection, _id, body):
#     ordem_compra = json.loads(ordem_compra_service.listar_ordem_compra_by_id(_id).to_json())
#     log = {}
#     for key, value in body.items():
#         if key in ordem_compra:
#             log[key] = value
#
#     if len(log) == 0:
#         pass
#     else:
#         log_model.Log(collection=collection,
#                       document_id=_id,
#                       old_values=log,
#                       last_updated_at=datetime.now(),
#                       created_at=datetime.now()).save()


# def log_atualizacao_equipamento(collection, _id, body):
#     equipamento = json.loads(equipamento_service.listar_equipamento_by_id(_id).to_json())
#     log = {}
#     for k, v in body.items():
#         if k in equipamento:
#             if equipamento[k] != v:
#                 log[k] = v
#
#     if len(log) == 0:
#         pass
#     else:
#         log_model.Log(collection=collection,
#                       document_id=_id,
#                       old_values=log,
#                       last_updated_at=datetime.now(),
#                       created_at=datetime.now()).save()


# def log_atualizacao_ordem_servico(collection, _id, updated_body):
#     old_ordem_servico = json.loads(ordem_servico_service.listar_ordem_servico_by_id(_id).to_json())
#     log_dt = {}
#     for updated_key, updated_value in updated_body.items():
#         if updated_key == 'triagem':
#
#             for updated_triagem_key, updated_value_triagem in updated_body['triagem'].items():
#
#                 if updated_triagem_key in old_ordem_servico['triagem'] and updated_body["triagem"][
#                     updated_triagem_key] != \
#                         old_ordem_servico['triagem'][updated_triagem_key]:
#
#                     if 'triagem' not in log_dt:
#                         log_dt['triagem'] = {}
#
#                     log_dt['triagem'][updated_triagem_key] = updated_value_triagem
#
#         if updated_key == 'diagnostico':
#
#             for updated_diagnostico_key, updated_diagnostico_value in updated_body['diagnostico'].items():
#                 if updated_diagnostico_key in old_ordem_servico['diagnostico'] and updated_body["diagnostico"][
#                     updated_diagnostico_key] != \
#                         old_ordem_servico['diagnostico'][updated_diagnostico_key]:
#
#                     if 'diagnostico' not in log_dt:
#                         log_dt['diagnostico'] = {}
#
#                     log_dt['diagnostico'][updated_diagnostico_key] = updated_diagnostico_value
#
#         if updated_key in old_ordem_servico and old_ordem_servico[updated_key] != updated_value:
#             log_dt[updated_key] = updated_value
#
#     if len(log_dt) == 0:
#         pass
#     else:
#         log_model.Log(collection=collection,
#                       document_id=_id,
#                       old_values=log_dt,
#                       last_updated_at=datetime.now(),
#                       created_at=datetime.now()).save()


# def log_atualizacao_movimentacao(collection, _id, body):
#     movimentacao = json.loads(movimentacao_service.listar_movimentacao_id(_id).to_json())
#     log = {}
#     for k, v in body.items():
#         if k in movimentacao:
#             if movimentacao[k] != v:
#                 log[k] = v
#
#     if len(log) == 0:
#         pass
#     else:
#         log_model.Log(collection=collection,
#                       document_id=_id,
#                       old_values=log,
#                       last_updated_at=datetime.now(),
#                       created_at=datetime.now()).save()


# def log_queries(body):
#     parsed_query_dt = query_parser.parse(body["where"])
#
#     if not "select" in body:
#         body["select"] = []
#
#     filted_log_list = log_model.Log.objects(
#         __raw__=parsed_query_dt).only(*body["select"])
#
#     return filted_log_list.to_json()


# def log_register(document_name, new_object_df, old_object_df):
#     log_dt = {}
#     pass


def registerLog(documento_name, antigo, novo, ignored_fields):
    document_id = antigo["_id"]["$oid"]
    del antigo["_id"]
    log = check_fields(antigo, novo, ignored_fields)
    if not log:
        print("There are not changes")
        pass
    else:
        print("Changes" + str(log))

        log_model.Log(collection=documento_name,
                      document_id=ObjectId(document_id),
                      old_values=json.dumps(log),
                      last_updated_at=datetime.now(),
                      created_at=datetime.now()).save()


def check_fields(antigo, novo, ignorated_fields):
    log = {}
    if type(novo) != dict:
        if type(antigo) == dict or type(antigo) == list:
            return antigo

        return antigo == novo

    for campo in novo.keys():
        if campo in ignorated_fields:
            continue

        if campo not in antigo:
            continue

        if type(antigo[campo]) == dict:
            _log = check_fields(antigo[campo], novo[campo], ignorated_fields)
            if _log:
                log[campo] = _log

            continue

        if type(antigo[campo]) == list:
            for indice in range(len(novo[campo])):
                _log = check_fields(antigo[campo][indice],
                                    novo[campo][indice], ignorated_fields)

                if _log:
                    if campo not in log:
                        log[campo] = {}
                    log[campo][indice] = _log

            continue

        if novo[campo] == antigo[campo]:
            continue

        log[campo] = antigo[campo]

    if len(log.keys()) == 0:
        return False

    return log
