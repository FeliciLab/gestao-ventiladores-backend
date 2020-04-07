# gestao-ventiladores-backend


## Tutorial
### Requisitos:
- Python (Versão superior 3.7)
- Virtualenv
- MongoDB

### 1 - Criar e ativar o ambiente virtual:
Windows
virtualenv <nome_da_virtualenv>
<nome_da_virtualenv>\Scripts\activate

Ubuntu
python3 -m venv <nome_da_virtualenv>
source <nome_da_virtualenv>/bin/activate

### 2 - Instalação dos módulos python:
pip install -r requirements.txt

### 3 - Export a variável de ambiente:
set FLASK_APP=run.py (Windows)
export FLASK_APP=run.py (Ubuntu)

### 4 - Execute a api:
python run.py

## API

"url": "localhost:5000/api/equipamentos" #rota
"method": "GET"

"url": "localhost:5000/api/equipamentos/2" #rota + esse 2 é o valor OS
"method": "GET

### fazer cadastro de triagem (form 1)
```json
"url": "localhost:5000/api/equipamentos" #rota
"method": "POST"
"header" : "Content-Type": "application/json"
"body": 
	{
		"numero_ordem_servico":"1",
	  	"triagem":{
	          "foto_equipamento_chegada":"foto1",
	          "tipo":"tipo1",
	          "unidade_de_origem":"origem1",
	          "numero_do_patrimonio":"numeropatrimonio1",
	          "numero_de_serie":"numero1",
	          "instituicao_de_origem":"1",
	          "responsavel_contato_da_instituicao_de_origem":"1",
	          "estado_de_conservacao":"1",
	          "marca":"1",
	          "modelo":"1",
	          "acessorios":"1",
	          "foto_apos_limpeza":"1",
	          "observacao":"1",
	          "responsavel_pelo_preenchimento":"1"
	          }
	}
```
			
### fazer avaliacao clinica (form 2)
```json
"url": "localhost:5000/api/equipamentos/2", #rota + esse 2 é o valor OS
"method": "PUT"
"header" : "Content-Type": "application/json"
"body": 
	{	
		"clinico": {
		"classificao_ventilador": "x",
		"resultados_do_teste": "x",           
		"acessorios_necessitados": "x"       
		}
	}


# fazer avaliacao tecnico (form 3)

"url": "localhost:5000/api/equipamentos/2", #rota + esse 2 é o valor OS
"method": "PUT"
"header" : "Content-Type": "application/json"
"body": 
	{	
		"tecnico": {
			"resultado_do_teste": "x",
			"demanda_por_insumo": "x",
			"demanda_por_servico": "x"
		}
	}
```

### fabricante e modelo

```json
"url": "localhost:5000/api/fabricantes" #rota + esse CONSUL é o fabricante
"method": "GET

"url": "localhost:5000/api/fabricantes/CONSUL" #rota + esse CONSUL é o fabricante
"method": "GET

"url": "localhost:5000/api/fabricantes" #rota
"method": "POST"
"header" : "Content-Type": "application/json"
"body": 
	{
	   "fabricante_nome": "fabricante",
	   "modelo": ["modelo a", "modelo b"]
	}

"url": "localhost:5000/api/fabricantes" #rota
"method": "PUT"
"header" : "Content-Type": "application/json"
"body": 
	{
		"fabricante_nome": "fabricante",
	    "modelo": ["modelo a", "modelo b"]
	}
```
