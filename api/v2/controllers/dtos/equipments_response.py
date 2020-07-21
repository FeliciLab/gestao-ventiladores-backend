from .utils import parser_mongo_response_to_list


class EquipmentsResponse:

    def __init__(self, equipments_list):
        self.equipments = equipments_list

    @property
    def get_equipments(self):
        return parser_mongo_response_to_list(self.equipments)
