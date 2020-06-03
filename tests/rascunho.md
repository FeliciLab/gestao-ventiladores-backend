# Rascunho de testes

## Rotas
### Assinatura da rota
* Cabeçalhos (Headers) se estão corretos:
  * `Content-Type: application/json` é enviado  
    (verificar utilização de middleware)
* Os métodos HTTP estão implementados:
  * One:
    * GET, PUT, PATCH, DELETE
  * Many:
    * GET, POST, PUT, PATCH, DELETE
  * Find:
    * POST

### Responses
* Se as respostas contêm um json
* Não contém $oid, $date
* Resposta Sucesso contém o campo "result"
* Resposta Erro contém o campo "error"
* Many:
  * GET/POST:
    * Retorna uma lista no json
  * POST/PUT/DELETE body tem que ser vazio
* One:
  * GET retorna um objeto dentro de `result`
  * PUT/PATCH/DELETE:
    * retorna somente o status 200 se OK
    * retorna status 400 com o erro dentro de `error`


#### Validação dos Parameters
* One:
  * O _id tem que ser string
  * O _id pode ser convertido para ObjectId
  * O _id existe no banco
* Many:
  * GET
    * Se deleted: 
        * validar se o campo deleted é true or false
  * POST/PUT/PATCH/DELETE:
    * Verifica se há o campo `content`
    * verificar se há array dentro do campo `content` no body
  * PUT/PATCH/DELETE:
    * O campo _id existe
    * O valor do campo _id é valido
    * O _id existe no banco


```
{ "error": [{ indice: 1 erro: "" }] }
{ "result": [] }

#parametros
{ "content": {} }
[]

if (data.result)

if valido
  verifico_parametro (array [''], body)
  temErro
  errors = []
  for
    varifico validade dos campos (body, schema)
    temErro = True
    1 2 3 4 6 ... 30 error ... 100
  
  if temErro
  return {
    error: [
      {
        indice: 30
        erro: validation
      } 
      {
        indice: 45
        erro: validation
      }
    ]
  }

executar_funcao:
  return jsonify({
    "oqueeuquero": resultado
  })

{
  statu: 200
  data: resultado
}

if (data.error) {
  throw error
}

if (data.success) {
  return data.success
}

log:
{
  error: "faiô"
}
```