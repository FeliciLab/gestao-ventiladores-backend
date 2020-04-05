from views import equipamento_view, usuario_view

def initialize_routes(api):
    api.add_resource(equipamento_view.EquipamentoList, '/api/equipamentos')
    api.add_resource(equipamento_view.EquipamentoDetail, '/api/equipamentos/<id>')
    api.add_resource(usuario_view.UsuarioList, '/api/usuarios')