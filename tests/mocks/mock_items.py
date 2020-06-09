# Nome unidade e quantidade (obrigatórios)
mock_items = {
    "sem_obrigatorios": {
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
        "created_at": "2020-06-05T15:46:37.204Z",
        "updated_at": "2020-06-05T15:46:37.204Z"
    },

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
}
