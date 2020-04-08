from api.views import equipamento_view, fabricante_view

def initialize_routes(api):
    api.add_resource(equipamento_view.EquipamentoList, '/api/equipamentos')
    api.add_resource(equipamento_view.EquipamentoDetail, '/api/equipamento/<numero_ordem_servico>')

    api.add_resource(equipamento_view.EquipamentoImportacao, '/api/equipamentos/equipamentosimportacao')

    api.add_resource(fabricante_view.FabricanteList, '/api/fabricantes')
    api.add_resource(fabricante_view.FabricanteDetail, '/api/fabricante/<fabricante_nome>')
    #api.add_resource(usuario_view.UsuarioList, '/api/usuarios')
