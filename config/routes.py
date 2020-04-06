from api.views import equipamento_view


def initialize_routes(api):
    api.add_resource(equipamento_view.EquipamentoList, '/api/equipamentos')
    api.add_resource(equipamento_view.EquipamentoDetail, '/api/equipamentos/<numero_ordem_servico>')
    #api.add_resource(usuario_view.UsuarioList, '/api/usuarios')
