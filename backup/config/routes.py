from views import triagem_view, usuario_view

def initialize_routes(api):
    api.add_resource(triagem_view.TriagemList, '/api/equipamentos')
    api.add_resource(triagem_view.TriagemDetail, '/api/equipamentos/<id>')
    api.add_resource(usuario_view.UsuarioList, '/api/usuarios')