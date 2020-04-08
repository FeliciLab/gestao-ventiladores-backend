from pipenv.vendor import requests
import csv
from urllib.request import urlopen
import pandas as pd


class ImportadorDeEquipamentos():
    pass


def tratar_importacao(body):
    if "url_triagens" in body:
        url_triagens = body["url_triagens"]
        triagens_df = pd.read_csv(url_triagens)

        for index_linha, linha in triagens_df.iterrows():
            body = {
                "numero_ordem_servico": linha["Número da Ordem de Serviço"],
                "data_hora": linha["Carimbo de data/hora"],
                "triagem": {
                    "foto_equipamento_chegada": linha["Fotografe o equipamento no momento da chegada: "],
                    "tipo": linha["Selecione o tipo do equipamento:"],
                    "unidade_de_origem": linha["Selecione a unidade de origem do equipamento:"],
                    "numero_do_patrimonio": linha["Se público, informe o número do patrimônio:"],
                    "numero_de_serie": linha["Informe o número de série:"],
                    "instituicao_de_origem": linha["Informe o nome da instituição de origem:"],
                    "responsavel_contato_da_instituicao_de_origem": linha[
                        "Informe o responsável e o contato da institução de origem:"],
                    "estado_de_conservacao": linha["Selecione o estado de conservação do equipamento"],
                    "marca": linha["Selecione a marca do equipamento:"],
                    "modelo": linha["Selecione o modelo do equipamento"],
                    "acessorios": linha["Selecione os acessórios do equipamento que o acompanha:"],
                    "foto_apos_limpeza": linha["Fotografe o equipamento após a limpeza: "],
                    "observacao": linha["Se preciso, deixe uma observação:"],
                    "responsavel_pelo_preenchimento": linha["Responsável pelo Preenchimento"]
                }
            }

        #  response = urlopen(url_triagens)
        #  cr = csv.reader(response)
        #  for row in cr:
        #      print(row)
        # # pd.read_csv(cr)
        #  #triagens_csv = requests.get(url_triagens)

        pass
    elif "url_diagnosticos_clinicos" in body:
        pass
    elif "url_diagnosticos_tecnicos" in body:
        pass
    else:
        return {"erro": "Erro no body. Verificar o json enviado no body."}

    return {"ok": "Importacao realizada com sucesso"}
