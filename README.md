# gestao-ventiladores-backend


## Tutorial
### Requisitos:
- Python (Versão superior 3.7)
- Virtualenv
- MongoDB

### 1 - Criar e ativar o ambiente virtual:
Windows
```
virtualenv <nome_da_virtualenv>
<nome_da_virtualenv>\Scripts\activate
```

Ubuntu
```
python3 -m venv <nome_da_virtualenv>
source <nome_da_virtualenv>/bin/activate
```

### 2 - Instalação dos módulos python:
```
pip install -r requirements.txt
```

### 3 - Export a variável de ambiente:
Windows
```
set FLASK_APP=run.py
```
Ubuntu
```
export FLASK_APP=run.py
```
### 4 - Execute a api:
```
python run.py
```

## API

### Retornar todos os equipamentos
```json
"url": "localhost:5000/api/equipamentos"
"method": "GET"
```

### Retornar um equipamentoe específico
```json
"url": "localhost:5000/api/equipamentos/<numero_ordem_servico>"
"method": "GET
```

### Fazer cadastro do equipamento - triagem (form 1)
```json
"url": "localhost:5000/api/equipamentos"
"method": "POST"
"header" : "Content-Type": "application/json"
"body": 
	{
	  "numero_ordem_servico": "1",
	  "created_at":"2020-04-09T21:20:23.61",
	  "updated_at":"2020-04-09T21:20:23.61",
	  "status": "string",
	  "triagem": {
	    "nome_equipamento": "string",
	    "foto_equipamento_chegada": "string",
	    "tipo": "string",
	    "unidade_de_origem": "string",
	    "numero_do_patrimonio": "string",
	    "numero_de_serie": "string",
	    "instituicao_de_origem": "string",
	    "nome_responsavel": "string",
	    "contato_responsavel": "string",
	    "estado_de_conservacao": "string",
	    "fabricante": "string",
	    "marca": "string",
	    "modelo": "string",
	    "acessorios": [
	      {
		"descricao": "Blender",
		"acompanha": true,
		"quantidade": 1,
		"estado_de_conservacao": "string"
	      },
	      {
		"descricao": "Braço articulado",
		"acompanha": true,
		"quantidade": 1,
		"estado_de_conservacao": "string"
	      }
		],
	    "foto_apos_limpeza": "string",
	    "observacao": "string",
	    "responsavel_pelo_preenchimento": "string"
	  }
}
```

### Fazer diagnostico - clinico/tecnico (form 2)
```json
"url": "localhost:5000/api/equipamentos/<numero_ordem_servico>"
"method": "PUT"
"header" : "Content-Type": "application/json"
"body": 
{
  "diagnostico": {
    "resultado_tecnico": "string",
    "demanda_servicos": "string",
    "demanda_insumos": "string",
    "acao_orientacao": "string",
    "observacoes": "string",
    "acessorios_extras": [
    	{
    		"quantidade": 0 ,
    		"nome": "string"
    		
    	}
    ],
    "itens": [
      {
        "nome": "string",
        "tipo": "",
        "quantidade": 0,
        "descricao": "string",
        "valor": 0.00,
        "prioridade": ""
      }
    ]
  }
}

```

### Retornar os equipamentos pelo seu status
```json
"url": "localhost:5000/api/equipamentos/find"
"method": "POST"
"header" : "Content-Type": "application/json"
"body": 
{
	"status":"string"
}

```

### Fazer importacao da triagem
```json
"url": "localhost:5000/api/importar/triagem"
"method": "POST"
"header" : "Content-Type": "application/json"
"body": 
	{
	    "url_triagens": "<url_triagens>"
	}
```

### Fazer importacao do diagnostico
```json
"url": "localhost:5000/api/importar/diagnostico"
"method": "POST"
"header" : "Content-Type": "application/json"
"body": 
	{
	    "url_triagens": "<url_triagens>"
	}
```
