from bson import ObjectId
from ..models import log_model
from datetime import datetime


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


def registerLog(documento_name,
                antigo,
                novo,
                ignored_fields=None,
                all_fields=True):

    if ignored_fields is None:
        ignored_fields = []

    document_id = antigo["_id"]["$oid"]
    del antigo["_id"]
    log = check_fields(antigo, novo, all_fields, ignored_fields)
    if not log:
        print("There are not changes")
        return None

    print("Changes" + str(log))
    log = formatLog(log)
    log_model.Log(
        collection=documento_name,
        document_id=ObjectId(document_id),
        old_values=log,
        last_updated_at=datetime.now(),
        created_at=datetime.now(),
    ).save()


def formatLog(log):
    for key in log.keys():
        if "$oid" == key:
            return log[key]
        if "$date" == key:
            return log[key]
        if type(log[key]) == dict:
            log[key] = formatLog(log[key])
        if type(log[key]) == list:
            for element in log[key]:
                if type(element) == dict:
                    log[key] = formatLog(element)
    return log


def check_fields(antigo, novo, all_fields, ignorated_fields=None):
    if ignorated_fields is None:
        ignorated_fields = []

    log = {}
    if type(novo) != dict:
        if type(antigo) == dict or type(antigo) == list:
            return antigo

        return antigo == novo

    for campo in antigo.keys():
        if campo in ignorated_fields:
            continue

        if campo not in novo:
            if all_fields:
                log[campo] = antigo[campo]

            continue

        if not isinstance(novo[campo], antigo[campo]):
            log[campo] = antigo[campo]
            continue

        if type(novo[campo]) == dict and type(antigo[campo]) == dict:
            _log = check_fields(
                antigo[campo], novo[campo], all_fields, ignorated_fields
            )
            if _log:
                log[campo] = _log

            continue

# if type(novo[campo]) == dict and type(novo[campo]) != type(antigo[campo]):
#     log[campo] = antigo[campo]
#     continue

        if type(novo[campo]) == list and type(antigo[campo]) == list:
            if len(novo[campo]) != len(antigo[campo]):
                log[campo] = antigo[campo]
            else:
                for indice in range(len(antigo[campo])):
                    _log = check_fields(
                        antigo[campo][indice],
                        novo[campo][indice],
                        all_fields,
                        ignorated_fields,
                    )

                    if _log:
                        if campo not in log:
                            log[campo] = {}
                        log[campo][str(indice)] = _log

            continue

# if type(novo[campo]) == list and type(novo[campo]) != type(antigo[campo]):
#     log[campo] = antigo[campo]
#     continue

        if novo[campo] == antigo[campo]:
            continue

        log[campo] = antigo[campo]

    if len(log.keys()) == 0:
        return False

    return log
