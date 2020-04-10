import pandas as pd
from ..services.equipamento_service import registrar_equipamento
import numpy as np

class ImportadorDeEquipamentos():
    pass

def tratar_importacao(body):
    if "url_triagens" in body:
        url_triagens = body["url_triagens"]
        triagens_df = pd.read_csv(url_triagens)
        triagens_df = triagens_df.replace(np.nan, '', regex=True)

        for index_linha, linha in triagens_df.iterrows():
            body = {
                "numero_ordem_servico": str(linha["Número da Ordem de Serviço"]),
                "created_at": __transformando_data(linha["Carimbo de data/hora"]),
                "updated_at": __transformando_data(linha["Carimbo de data/hora"]),
                "status": "triagem",
                "triagem": {
                    "nome_equipamento": "",  # it field does not exist in csv
                    "foto_equipamento_chegada": __get_url_da_primeira_foto(
                        linha["Fotografe o equipamento no momento da chegada: "]),
                    "tipo": linha["Selecione o tipo do equipamento:"],
                    "unidade_de_origem": linha["Selecione a unidade de origem do equipamento:"],
                    "numero_do_patrimonio": str(linha["Se público, informe o número do patrimônio:"]),
                    "numero_de_serie": linha["Informe o número de série:"],
                    "instituicao_de_origem": linha["Informe o nome da instituição de origem:"],
                    "nome_responsavel": linha["Informe o responsável e o contato da institução de origem:"],
                    "contato_responsavel": "",  # it field does not exist in csv
                    "estado_de_conservacao": linha["Selecione o estado de conservação do equipamento"],

                    "fabricante": linha["Selecione a marca do equipamento:"],
                    "marca": linha["Selecione a marca do equipamento:"],
                    "modelo": linha["Selecione o modelo do equipamento"],
                    "acessorios": __get_acessorios(linha["Selecione os acessórios do equipamento que o acompanha:"]),
                    "foto_apos_limpeza": __get_url_da_primeira_foto("Fotografe o equipamento após a limpeza: "),
                    "observacao": linha["Se preciso, deixe uma observação:"],
                    "responsavel_pelo_preenchimento": linha["Responsável pelo Preenchimento"]
                }
            }

            registrar_equipamento(body)

        return {"ok": "Importacao realizada com sucesso"}
    elif "url_diagnosticos_clinicos" in body:
        pass
    elif "url_diagnosticos_tecnicos" in body:
        pass
    else:
        return {"erro": "Erro no body. Verificar o json enviado no body."}

#
# def transforma_string_em_lista(dado):
#     if isinstance(dado, str):
#         return [dado]

def __transformando_data(data):
    data = data[6:10] + data[2:6] + data[:2] + data[10:]
    data = data.replace('/', '-').replace(' ', 'T')
    return data

def __get_acessorios(acessorios_string):
    if acessorios_string is "":
        return []

    acessorio_list = list()
    for acessorio_string in acessorios_string.split(", "):
        acessorio_dt = {
                "descricao": acessorio_string,
                "acompanha": 'true',
                "quantidade": 1,
                "estado_de_conservacao": ""
            }

        acessorio_list.append(acessorio_dt)

    return acessorio_list

def __get_url_da_primeira_foto(url_fotos_string):
    if url_fotos_string is "":
        return ""
    return url_fotos_string.split(",")[0]
