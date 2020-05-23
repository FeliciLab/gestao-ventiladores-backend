from tests.base_case import BaseCase
from unittest import main
import json


class Equipment(BaseCase):
    def test_create_new_equipment_successful(self):
        data = json.dumps([
                {
                    "contato_responsavel": "string",
                    "created_at": "2020-05-23T13:29:27.892Z",
                    "fabricante": "string",
                    "marca": "string",
                    "modelo": "string",
                    "municipio_origem": "string",
                    "nome_equipamento": "string",
                    "nome_instituicao_origem": "string",
                    "nome_responsavel": "string",
                    "numero_de_serie": "haha deu certo",
                    "numero_do_patrimonio": "string",
                    "status": "string",
                    "tipo": "string",
                    "tipo_instituicao_origem": "string",
                    "updated_at": "2020-05-23T13:29:27.893Z"
                },
                    {
                    "contato_responsavel": "string",
                    "created_at": "2020-05-23T13:29:27.892Z",
                    "fabricante": "string",
                    "marca": "string",
                    "modelo": "string",
                    "municipio_origem": "string",
                    "nome_equipamento": "string",
                    "nome_instituicao_origem": "string",
                    "nome_responsavel": "string",
                    "numero_de_serie": "blablaasdas123",
                    "numero_do_patrimonio": "string",
                    "status": "string",
                    "tipo": "string",
                    "tipo_instituicao_origem": "string",
                    "updated_at": "2020-05-23T13:29:27.893Z"
                }
        ])

        response = self.app.post('/api/equipments',
                      headers={"Content-Type": "application/json"},
                      data=data)
        
        self.assertEqual(type(response), list)
        self.assertEqual(response.status_code, 200)


main()
