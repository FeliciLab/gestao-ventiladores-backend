from unittest import TestCase
from unittest.mock import patch
from run import app
from api.v2.controllers.equipments_controller import EquipmentsController
from api.v2.services.equipments_service import EquipmentsService
from ..models.builder.equipment_builder import EquipmentBuilder
from tests.mocks.mock_items import mock_items
from api.v2.controllers.dtos.equipments_response import EquipmentsResponse


def mock_equipaments():
    def set_and_get(data_eqp):
        equipment_builder = EquipmentBuilder()
        equipment_builder.set_equipamento(data_eqp)
        return equipment_builder.get_equipamento()

    return [set_and_get(data_equip) for data_equip in mock_items["dados_de_equipamentos"]]


class EquipmentsControllerTest(TestCase):

    def setUp(self) -> None:
        self.client = app.test_client()

    @patch.object(EquipmentsService, 'get_all', return_value=mock_equipaments())
    def test_controller_calls_get_method(self, mock_get_all):
        EquipmentsController().get()
        mock_get_all.assert_called_once()

    def test_response_has_correct_format(self):
        list_equipments = mock_equipaments()
        equip_response = EquipmentsResponse(list_equipments).get_equipments

        equip_keys = ("numero_de_serie",
                      "nome_equipamento",
                      "status",
                      "numero_do_patrimonio",
                      "tipo",
                      "fabricante",
                      "municipio_origem",
                      "nome_instituicao_origem",
                      "tipo_instituicao_origem",
                      "nome_responsavel",
                      "contato_responsavel")

        for equip in equip_response:
            for key in equip_keys:
                self.assertTrue(key in equip)
