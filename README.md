# gestao-ventiladores-backend
Este repositório implementa parte do projeto "SMART Health: suporte à tomada de decisão inteligente de profissionais da saúde e gestores no combate à transmissão da COVID-19 no Ceará", desenvolvido pela Escola de Saúde Pública do Ceará (ESP-CE) em parceria com o Grupo de Engenharia de Software Adaptativo e Distribuído (GESAD) da UECE. 

O projeto tem como objetivo principal o desenvolvimento de soluções tecnológicas que auxiliem profissionais de saúde no combate à transmissão do COVID-19 e promovam a tomada de decisão por gestores, facilitando assim o trabalho desses profissionais.

Relacionados a este repositório, destaca-se o seguinte objetivo específico:
- Implementar um sistema de gerenciamento e alocação dos ventiladores mecânicos.


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

### 3 - Exporte a variável de ambiente:
Windows
```
set FLASK_APP=run.py
```
Ubuntu ou Mac
```
export FLASK_APP=run.py
```
### 4 - Configure seu banco local:
Crie o arquivo env_config.py dentro de gestao-ventiladores-backend e insira.
```
# env_config.py
mongodb_host = 'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false'
```

### 5 - Execute a api:
```
python run.py
```

## API

### Toda documentação da API pode ser encontrada acessando a rota abaixo:
http://127.0.0.1:5000/apidocs

