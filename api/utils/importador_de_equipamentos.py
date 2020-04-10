import pandas as pd
from api.services.equipamento_service import registrar_equipamento
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
                    "fabricante": linha["Selecione a marca do equipamento:"],
                    "marca": linha["Selecione a marca do equipamento:"],
                    "modelo": linha["Selecione o modelo do equipamento"],
                    "acessorios": linha["Selecione os acessórios do equipamento que o acompanha:"],
                    "foto_apos_limpeza": linha["Fotografe o equipamento após a limpeza: "],
                    "observacao": linha["Se preciso, deixe uma observação:"],
                    "responsavel_pelo_preenchimento": linha["Responsável pelo Preenchimento"]
                }
            }
            body['triagem']['foto_equipamento_chegada'] = transforma_string_em_lista(
                body['triagem']['foto_equipamento_chegada'])
            body['triagem']['foto_apos_limpeza'] = transforma_string_em_lista(
                body['triagem']['foto_apos_limpeza'])
            body['triagem']['acessorios'] = body['triagem']['acessorios'].split(',')
            for i in range(len(body['triagem']['acessorios'])):
                body['triagem']['acessorios'][i] = body['triagem']['acessorios'][i].strip()

            registrar_equipamento(body)

    elif "url_diagnosticos_clinicos" in body:
        pass
    elif "url_diagnosticos_tecnicos" in body:
        pass
    else:
        return {"erro": "Erro no body. Verificar o json enviado no body."}

    return {"ok": "Importacao realizada com sucesso"}


def transforma_string_em_lista(dado):
    if isinstance(dado, str):
        return [dado]
