from typing import Dict


def deepen(parent_key, parent_dict):
    dotted_dict = parent_dict.copy()
    for key, value in parent_dict.items():
        if isinstance(value, Dict):
            result = deepen(parent_key + "." + key, value)
            del dotted_dict[key]
            dotted_dict.update(result)
        else:
            del dotted_dict[key]
            dotted_dict.update({parent_key + "." + key: value})

    return dotted_dict


def clean(dotted_query_body):
    new_dict = {}
    for key, value in dotted_query_body.items():
        new_dict.update({key.replace("$.", ""): value})
    return new_dict


class OrdemServicoQueryParser:

    @staticmethod
    def parse(query_body):
        dotted_query_body = deepen("$", query_body)
        adapted_query_body = clean(dotted_query_body)
        return adapted_query_body


