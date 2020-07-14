mock_service_orders = {
    "service_order_with_id": {"_id": "2020-06-05T15:46:37.204Z"},
    "service_order_with_updated": {"updated_at": "2020-06-05T15:46:37.204Z"},
    "service_order_with_deleted": {"deleted_at": "2020-06-05T15:46:37.204Z"},
    
    "complete": {
        "equipamento_id": "5ecc5e521ef64069c005338a",
        "numero_ordem_servico": 999,
        "status": "triagem",
        "triagem": {
            "estado_de_conservacao": "teste",
            "acessorios": [
                {
                    "item_id": "5f071f24ac5199d80ddac5ed",
                    "quantidade": 1,
                    "acompanha": True,
                },
            ],
        },
        "diagnostico": {
            "resultado_tecnico": "top",
            "itens": [{"item_id": "5f071f24ac5199d80ddac5ed", "quantidade": 1},],
        },
        "calibragem": {"status": "TESTE"},
    },

    "complete_to_mockito": {
        "equipamento_id": "5ecc5e521ef64069c005338a",
        "numero_ordem_servico": "0999",
        "status": "triagem",
        "triagem": {
            "estado_de_conservacao": "teste",
            "acessorios": [
                {
                    "item_id": "5f071f24ac5199d80ddac5ed",
                    "quantidade": 1,
                    "acompanha": True,
                },
            ],
        },
        "diagnostico": {
            "resultado_tecnico": "top",
            "itens": [{"item_id": "5f071f24ac5199d80ddac5ed", "quantidade": 1},],
        },
        "calibragem": {"status": "TESTE"},
    },

    "correct_patch": {
        "_id": "5ee37c19d86b6a8893d1a3a7",
        "status": "diagnostico",
        "calibragem": {"status": "TESTE - OK"},
    }, 

    "correct_patch_mockito": {
        "status": "diagnostico",
        "calibragem": {"status": "TESTE - OK"},
    }

}
