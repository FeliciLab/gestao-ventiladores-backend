template = {
  "swagger": "2.0",
  "info": {
    "title": "Central de Ventiladores API",
    "description": "This is the documentation to API used in 'Central de Ventiladores'",
    "contact": {
      "responsibleOrganization": "Escola de Saúde Pública do Ceará",
      "url": "https://github.com/EscolaDeSaudePublica",
    },
    "version": "2.0",
    "openapi": "3.0.n"
  },
  "host": "https://gestao-ventiladores.dev.org.br/",
  "schemes": [
    "http",
    "https"
  ],
  "operationId": "getmyData"
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'centralventiladores',
            "route": '/centralventiladores.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/v2/apidocs/"
}
