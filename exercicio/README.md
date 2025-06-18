Listar tarefas (GET /tarefas)
-> [ ] - Se o retorno do código de status é 200
-> [ ] - Se o .json retornado é uma instancia do tipo list
-> [ ] - Se a quantidade de elementos retornado é maior que 0

Teste criar nova tarefa (POST /tarefas)
-> [ ] - Se o retorno do código de status é 201
-> [ ] - Testar se o ID da reposta do JSON não é None
-> [ ] - Verificar se no json retornado o valor da chave "tarefa" é o mesmo que você especificou em assert

Teste obter tarefa existente (GET /tarefas/<id>)
-> [ ] - Se o retorno do código de status é 200
-> [ ] - Se o ID do json retornado é igual a 1

Teste obter tarefa inexistente (GET /tarefas/<id>)
-> [ ] - Se o retorno do código de status é 404
-> [ ] - Verificar se existe no JSON retornado a chave "erro" na tarefa informada

Teste atualizar tarefa (PUT /tarefas/<id>)
-> [ ] - Se o retorno do código de status é 200
-> [ ] - Verificar se no json retornado o valor da chave "tarefa" é o mesmo que você especificou em assert
-> [ ] - Verificar se no json retornado o valor da chave "feito" é o mesmo que você especificou em assert

Teste atualizar tarefa inexistente (PUT /tarefas/<id>)
-> [ ] - Se o retorno do código de status é 404
-> [ ] - Verificar se existe no JSON retornado a chave "erro" na tarefa informada

Teste remover tarefa (DELETE /tarefas/<id>)
-> [ ] - Se o retorno do código de status é 200 ao consultar a tarefa
-> [ ] - Verificar se ao consultar a tarefa deletada o codigo é 404

Teste remover tarefa inexistente (DELETE /tarefas/<id>)
-> [ ] - Se o retorno do código de status é 404
-> [ ] - Verificar se existe no JSON retornado a chave "erro" na tarefa informada

Teste campos obrigatórios ao criar tarefa
-> [ ] - Se o retorno do código de status é 400
-> [ ] - Verificar se existe no JSON retornado a chave "erro" na tarefa informada

[ ] Teste validação de tipos dos campos
-> [ ] - Se o retorno do código de status é 400
-> [ ] - Verificar se existe no JSON retornado a chave "erro" na tarefa informada
