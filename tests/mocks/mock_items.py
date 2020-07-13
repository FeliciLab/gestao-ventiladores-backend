# Nome unidade e quantidade (obrigatórios)
mock_items = {


    "valido": {
        "nome": "teste",
        "unidade_medida": "und",
        "quantidade": 1,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
        "created_at": "2020-06-05T15:46:37.204Z",
        "updated_at": "2020-06-05T15:46:37.204Z"
    },

    "com_deleted": {
        "nome": "teste",
        "unidade_medida": "und",
        "quantidade": 1,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
        "created_at": "$date",
        "updated_at": "$date",
        "deleted_at": "$date",
    },

    "sem_um_obrigatorio": {
        "nome": "",
        "unidade_medida": "und",
        "quantidade": 5,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
        "created_at": "$date",
        "updated_at": "$date"
    },

    "valido_sem_datas": {
        "nome": "teste",
        "unidade_medida": "und",
        "quantidade": 1,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
    },

    "valido_patch": {
        "nome": "teste",
        "tipo": "teste_patch",
        "descricao": "Estou testando"
    },

    "somente_obrigatorios": {
        "nome": "teste",
        "unidade_medida": "teste_patch",
        "quantidade": 5
    },

    "invalido_patch": {
        "unidade": 5
    },

    "campo_errado_put": {
        "nome": "teste",
        "unidade_medida": "und",
        "quantidade": 1,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao_blabla": "",
        "created_at": "2020-06-05T15:46:37.204Z",
        "updated_at": "2020-06-05T15:46:37.204Z"
    },

    "campo_extra_errado": {
        "blabla": "blabla",
        "nome": "teste",
        "unidade_medida": "und",
        "quantidade": 1,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
        "created_at": "2020-06-05T15:46:37.204Z",
        "updated_at": "2020-06-05T15:46:37.204Z"
    },

    "invalido_id": {
        "_id": "aa202020",
        "nome": "teste",
        "unidade_medida": "und",
        "quantidade": 1,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
        "created_at": "2020-06-05T15:46:37.204Z",
        "updated_at": "2020-06-05T15:46:37.204Z"
    },

    "inexistente_id": {
        "_id": "5ecc5e521ef64069c005338a",
        "nome": "teste",
        "unidade_medida": "und",
        "quantidade": 1,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
        "created_at": "2020-06-05T15:46:37.204Z",
        "updated_at": "2020-06-05T15:46:37.204Z"
    },

    "triagem_um": {
        "descricao": "Mangueira de Oxigênio (verde)",
        "acompanha": "true",
        "quantidade": 1,
        "estado_de_conservacao": ""
    },

    "triagem_formatado": {
        "traqueias": {
            "tipo": "acessorio",
            "descricao": "Traquéias",
            "acompanha": True,
            "quantidade": 49,
            "estado_de_conservacao": "",
            "reference_key": "traqueias"
        }
    },

    "objeto_item": {
        'tipo': 'acessorio',
        'nome': 'Traquéias',
        'quantidade': 49,
        'unidade_medida': 'und',
        'reference_key': 'traqueias'
    },
    "item_collection": {
        'tipo': 'acessorio',
        'fabricante': '',
        'codigo': '',
        'nome': 'Traquéias',
        'unidade_medida': 'und',
        'quantidade': 49,
        'descricao': '',
        'reference_key': 'traqueias'
    },

    "diagnostico": {
        "tipo": "insumo",
        "fabricante": "",
        "codigo": "",
        "nome": "Mangueira PU 6mm",
        "unidade_medida": "Metro",
        "quantidade": 1,
        "descricao": ""
    },
    "diagnostico_formatado":{
        'mangueirapu6mm': {
            'tipo': 'insumo',
            'fabricante': '',
            'codigo': '',
            'nome': 'Mangueira PU 6mm',
            'unidade_medida': 'Metro',
            'quantidade': 3,
            'descricao': '',
            'reference_key': 'mangueirapu6mm'
        }
    }

}
