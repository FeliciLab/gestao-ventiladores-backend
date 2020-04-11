from api.views import equipamento_view, fabricante_view, importador_view


def initialize_routes(api):
    api.add_resource(equipamento_view.EquipamentoList, '/api/equipamentos')
    api.add_resource(equipamento_view.EquipamentoDetail, '/api/equipamento/<numero_ordem_servico>')


    api.add_resource(importador_view.TriagemImportacao,'/api/importar/triagem')
    api.add_resource(importador_view.DiagnosticoClinicoETecnicoImportacao, '/api/importar/diagnostico')

   # api.add_resource(equipamento_view.EquipamentoImportacao, '/api/equipamentos/equipamentosimportacao')

    api.add_resource(fabricante_view.FabricanteList, '/api/fabricantes')
    api.add_resource(fabricante_view.FabricanteDetail, '/api/fabricante/<fabricante_nome>')
    #api.add_resource(usuario_view.UsuarioList, '/api/usuarios')
