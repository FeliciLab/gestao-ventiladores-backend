import json

import pandas as pd

from ..services import fabricante_service
from ..services.equipamento_service import registrar_equipamento
import numpy as np


class ImportadorDeEquipamentos():
    pass


def importar_triagem(body):
    try:
        if "url" in body:
            url = body["url"]
            triagens_df = pd.read_csv(url)
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

                        "acessorios": __get_acessorios(
                            linha["Selecione os acessórios do equipamento que o acompanha:"]),
                        "foto_apos_limpeza": __get_url_da_primeira_foto("Fotografe o equipamento após a limpeza: "),
                        "observacao": linha["Se preciso, deixe uma observação:"],
                        "responsavel_pelo_preenchimento": linha["Responsável pelo Preenchimento"]
                    }
                }

                __insert_or_update_fabricante_db(linha)

                registrar_equipamento(body)
    except Exception:
        return {"erro": Exception.__traceback__}

    return {"ok": "Importacao realizada com sucesso!"}

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


def __adicionar_nova_marca_e_modelo(marca_nome, modelo_nome, fabricante_dt):
    fabricante_dt["marcas"].append({"marca": marca_nome,
                                    "modelos": [modelo_nome]})

    del fabricante_dt["_id"]

    fabricante_service.atualizar_fabricante(fabricante_dt["fabricante_nome"], fabricante_dt)


def __adicionar_nova_modelo(marca_nome, modelo_nome, fabricante_dt):
    for marca_dt in fabricante_dt["marcas"]:
        if marca_nome == marca_dt["marca"]:
            marca_dt["modelos"].append(modelo_nome)

    del fabricante_dt["_id"]

    fabricante_service.atualizar_fabricante(fabricante_dt["fabricante_nome"], fabricante_dt)


def __update_fabricante_db(linha, fabricante_string):
    marca_nome = linha["Selecione a marca do equipamento:"].strip()
    modelo_nome = linha["Selecione o modelo do equipamento"].strip()
    fabricante_dt = json.loads(fabricante_string)
    if not any(marca_dt['marca'] == marca_nome for marca_dt in fabricante_dt["marcas"]):
        __adicionar_nova_marca_e_modelo(marca_nome, modelo_nome, fabricante_dt)

    elif not any((modelo_nome in marca_dt['modelos']) for marca_dt in fabricante_dt["marcas"]):
        __adicionar_nova_modelo(marca_nome, modelo_nome, fabricante_dt)


def __add_fabricate_db(linha):
    fabricante_nome = linha["Selecione a marca do equipamento:"].strip()
    marca_nome = linha["Selecione a marca do equipamento:"].strip()
    modelo_nome = linha["Selecione o modelo do equipamento"].strip()

    body = {
        "fabricante_nome": fabricante_nome,
        "marcas": [
            {
                "marca": marca_nome,
                "modelos": [modelo_nome]
            }

        ]
    }

    fabricante_service.registar_fabricante(body)


def __insert_or_update_fabricante_db(linha):
    fabricante_nome = linha["Selecione a marca do equipamento:"]

    fabricante_string = fabricante_service.listar_fabricante_id(fabricante_nome)

    if fabricante_string is not None:
        __update_fabricante_db(linha, fabricante_string)
    else:
        __add_fabricate_db(linha)


def importar_diagnostino_clinico_e_tecnico(body):
    try:
        if "url" in body:
            url = body["url"]

            triagens_df = pd.read_csv(url)
            triagens_df = triagens_df.replace(np.nan, '', regex=True)
    except Exception:
        return {"erro": Exception.__traceback__}

    return {"ok": "Importacao realizada com sucesso!"}
