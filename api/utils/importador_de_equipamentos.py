import json

import pandas as pd
from ..schemas import ordem_servico_schema
from ..services import fabricante_service, ordem_servico_service, equipamento_service
import numpy as np
from datetime import datetime


def importar_triagem(triagem_body):
    try:
        if "url" in triagem_body:
            url = triagem_body["url"]
            triagens_df = pd.read_csv(url)
            triagens_df = triagens_df.replace(np.nan, '', regex=True)

            for index_linha, linha in triagens_df.iterrows():

                numero_de_serie = linha["Informe o número de série:"]

                equipamento = equipamento_service.listar_equipamento_by_numero_de_serie(numero_de_serie)


                equipamento_body = {
                    "numero_de_serie": linha["Informe o número de série:"],
                    "nome_equipamento": "",  # it field does not exist in csv
                    "numero_do_patrimonio": str(linha["Se público, informe o número do patrimônio:"]),
                    "tipo": linha["Selecione o tipo do equipamento:"],
                    "marca": linha["Selecione a marca do equipamento:"],
                    "modelo": linha["Selecione o modelo do equipamento"],
                    "fabricante": linha["Selecione a marca do equipamento:"],
                    "municipio_origem": linha["Informe Cidade de origem: "],
                    "nome_instituicao_origem": linha["Informe o nome da instituição de origem:"],
                    "tipo_instituicao_origem": linha["Selecione a unidade de origem do equipamento:"],
                    "nome_responsavel": linha["Informe o responsável e o contato da institução de origem:"],
                    "contato_responsavel": "",  # it field does not exist in csv
                    "created_at": __transformando_data(linha["Carimbo de data/hora"]),
                    "updated_at": __transformando_data(linha["Carimbo de data/hora"]),
                }


                triagem_body = {
                    "numero_ordem_servico": str(linha["Número da Ordem de Serviço"]).zfill(4),
                    "created_at": __transformando_data(linha["Carimbo de data/hora"]),
                    "updated_at": __transformando_data(linha["Carimbo de data/hora"]),
                    "status": "triagem",
                    "triagem": {

                        "foto_antes_limpeza": __get_url_da_primeira_foto(
                            linha["Fotografe o equipamento no momento da chegada: "]),





                        "estado_de_conservacao": linha["Selecione o estado de conservação do equipamento"],





                        "acessorios": __get_acessorios(
                            linha["Selecione os acessórios do equipamento que o acompanha:"]),
                        "foto_apos_limpeza": __get_url_da_primeira_foto("Fotografe o equipamento após a limpeza: ")
                    }
                }

                # O erro está aqui
                #__insert_or_update_fabricante_db(linha)
                es = ordem_servico_schema.OrdemServicoSchema()
                et = ordem_servico_schema.TriagemSchema()
                ea = ordem_servico_schema.AcessorioSchema()
                erro_equipamento = es.validate(triagem_body)
                erro_triagem = et.validate(triagem_body["triagem"])
                if erro_equipamento:
                    return {'validate': erro_equipamento}
                elif erro_triagem:
                    return {'validate': erro_triagem}
                for acessorio in triagem_body["triagem"]["acessorios"]:
                    if ea.validate(acessorio):
                        return {'validate': acessorio}

                equipamento_ja_cadastrado = ordem_servico_service.listar_ordem_servico_by_numero_ordem_servico(triagem_body['numero_ordem_servico'])
                if equipamento_ja_cadastrado:
                    ordem_servico_service.atualizar_ordem_servico(triagem_body, triagem_body['numero_ordem_servico'])
                else:
                    ordem_servico_service.registrar_ordem_servico(triagem_body)
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


def __adapt_time(data_and_time_string):
    datetime_object = datetime.strptime(data_and_time_string, '%m/%d/%Y %H:%M:%S')
    return datetime_object.strftime("%Y-%m-%dT%H:%M:%S.000+00:00")


def importar_diagnostino(body):
    try:
        if "url" in body:
            url = body["url"]

            diagnosticos_df = pd.read_csv(url)
            diagnosticos_df = diagnosticos_df.replace(np.nan, '', regex=True)

            for index_linha, linha in diagnosticos_df.iterrows():
                if linha["OS N°:"] is "":
                    continue

                numero_ordem_servico = str(int(linha["OS N°:"])).zfill(4)
                body = {
                    "resultado_tecnico": linha["Defeito observado:"],
                    "demanda_servicos": "",
                    "demanda_insumos": linha["Insumos utilizados no diagnostico:"],
                    "acao_orientacao": linha["Açao:"],
                    "observacoes": linha["Observação: "],
                    "itens": __get_itens(linha["Demanda por peças: "]) + __get_acessorios_extras(linha["Acessórios que necessita: "]),

                }

                __atualizar_campo_update_at(numero_ordem_servico, linha["Timestamp"])

                ed = ordem_servico_schema.DiagnosticoSchema()
                et = ordem_servico_schema.ItemSchema()
                erro_diagnostico = ed.validate(body)
                if erro_diagnostico:
                    return {'validate': erro_diagnostico}
                for item in body["itens"]:
                    if et.validate(item):
                        return {'validate': item}

                ordem_servico_service.atualizar_ordem_servico(
                    {
                        "status": "diagnostico",
                        "updated_at": __adapt_time(linha["Timestamp"]),
                        "diagnostico": body
                    },
                    numero_ordem_servico)


    except Exception:
        return {"erro": Exception.__traceback__}

    return {"ok": "Importacao realizada com sucesso!"}


def __atualizar_campo_update_at(numero_ordem_servico, update_at):
    ordem_servico_service.atualizar_ordem_servico({"updated_at": update_at}, numero_ordem_servico)


def __get_acessorios_extras(acessorios_extras_string):
    if acessorios_extras_string is "":
        return []

    acessorios_extras_list = list()

    for quantidade_e_acessorio_extra_string in acessorios_extras_string.split("\n"):
        if quantidade_e_acessorio_extra_string is "":
            continue

        quantidade = int(quantidade_e_acessorio_extra_string[0:2])
        acessorio_extra_nome = quantidade_e_acessorio_extra_string[3:]

        acessorios_extras_list.append(
            {
                "quantidade": quantidade,
                "nome": acessorio_extra_nome.strip(),
                "tipo": "acessorio",
                "descricao": "",
                "valor": 0.0,
                "prioridade": "baixa",
                "unidade_medida": ""
            }
        )
    return acessorios_extras_list


def __get_itens(item_string):
    if item_string is "":
        return []

    item_list = list()
    separator_char = ","
    if "\n" in item_string in item_string:
        separator_char = "\n"

    for item_nome in item_string.split(separator_char):
        nome = item_nome
        item_list.append(
            {
                "nome": nome.strip(),
                "tipo": "pecas",
                "descricao": "",
                "valor": 0.0,
                "prioridade": "baixa",
                "quantidade": 1,
                "unidade_medida": ""
             }
        )
    return item_list