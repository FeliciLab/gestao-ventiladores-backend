from api.views import ordem_servico_view, fabricante_view, importador_view,\
     foto_view, equipamento_view, ordem_compra_view


def initialize_routes(api):
    api.add_resource(equipamento_view.EquipamentoList, '/api/equipamentos')
    api.add_resource(equipamento_view.EquipamentoDetail, '/api/equipamento/<_id>')

    api.add_resource(ordem_servico_view.OrdemServicoList, '/api/ordem_servicos')
    api.add_resource(ordem_servico_view.OrdemServicoDetail, '/api/ordem_servico/<_id>')
    api.add_resource(ordem_servico_view.OrdemServicoFind, '/api/ordem_servico/find')
    api.add_resource(ordem_servico_view.OrdemServicoQuery, '/api/ordem_servico/find') # Essa class nunca é chamada

    api.add_resource(importador_view.TriagemImportacao, '/api/importar/triagem')
    api.add_resource(importador_view.DiagnosticoImportacao, '/api/importar/diagnostico')
    api.add_resource(foto_view.TriagemImagem, '/api/importar/imagem')

    api.add_resource(fabricante_view.FabricanteList, '/api/fabricantes')
    api.add_resource(fabricante_view.FabricanteDetail, '/api/fabricante/<fabricante_nome>')

    api.add_resource(ordem_compra_view.NumeroOrdemServicoList, '/api/ordem_compra')
