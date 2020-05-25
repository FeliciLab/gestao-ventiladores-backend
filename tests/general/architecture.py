from tests.base_case import BaseCase
from unittest import main
import json
import os


class ArchitectureTest(BaseCase):
    def test_all_code_is_pep8(self):
        ...
    
    
    def test_entity_one_has_all_methods(self):
        ...
    

    def test_entity_many_has_all_methods(self):
        ...


    def test_entity_find_has_all_methods(self):
        ...


    def test_files_are_lowercase_and_separated_with_underscore(self):
        ...


    def test_all_directory_with_python_code_has___init__(self):
        output = [dI for dI in os.listdir('foo') if os.path.isdir(os.path.join('foo',dI))]
        print(output)


if __name__ == '__main__':
    main()


# def test_create_new_equipment_successful(self):
#     data = json.dumps([
#         {
#             "contato_responsavel": "string",
#             "created_at": "2020-05-23T13:29:27.892Z",
#             "fabricante": "string",
#             "marca": "string",
#             "modelo": "string",
#             "municipio_origem": "string",
#             "nome_equipamento": "string",
#             "nome_instituicao_origem": "string",
#             "nome_responsavel": "string",
#             "numero_de_serie": "haha deu certo",
#             "numero_do_patrimonio": "string",
#             "status": "string",
#             "tipo": "string",
#             "tipo_instituicao_origem": "string",
#             "updated_at": "2020-05-23T13:29:27.893Z"
#         }
#     ])

#     response = self.app.post('/api/equipments',
#                     headers={"Content-Type": "application/json"},
#                     data=data)

#     """ Testes para todos os tipos de verbos HTTPS """
#     all_rules = []
#     for rule in self.app.application.url_map.iter_rules():
#         if next(iter(rule.methods)) == 'POST':
#             ...# Faça algo

#         if next(iter(rule.methods)) == 'PUT':
#             ...# Faça algo

#         if next(iter(rule.methods)) == 'PATCH':
#             ...# Faça algo

#     """ Testes por Entidades """

#     self.assertEqual(response.is_json, True)
#     self.assertEqual(response.status_code, 200)
#     self.assertEqual(type(response.json), list)
