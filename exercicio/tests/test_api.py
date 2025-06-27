import pytest
from exercicio.app import app

def test_listar_tarefas(client): #Lista TODAS tarefas (GET)
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0

def test_criar_tarefa_sucesso(client): #Cria nova tarefa (POST)
    nova_tarefa = {"tarefa": "Aprender pytest", "feito": False}
    response = client.post("/tarefas", json=nova_tarefa)

    assert response.status_code == 201
    dados = response.json
    assert isinstance(dados, dict)
    assert dados["tarefa"] == "Aprender pytest"
    assert dados["feito"] is False
    assert "id" in dados

def test_criar_tarefa_campos_faltando(client): #Testa erro se houver algum campo faltando 
    response = client.post("/tarefas", json={"tarefa": "Sem feito"})
    assert response.status_code == 400
    assert "erro" in response.json

def test_criar_tarefa_tipos_invalidos(client): #Testa os tipos
    dados_invalidos = {"tarefa": 123, "feito": "não é booleano"}
    response = client.post("/tarefas", json=dados_invalidos)
    assert response.status_code == 400
    assert "erro" in response.json

def test_obter_tarefa_existente(client):#Testa pegar a tarefa pelo id
    response = client.get("/tarefas/1")
    assert response.status_code == 200
    assert response.json["id"] == 1

def test_obter_tarefa_inexistente(client):#Testa erro se a tarefa não existe
    response = client.get("/tarefas/9999")
    assert response.status_code == 404
    assert "erro" in response.json

def test_atualizar_tarefa_existente(client):#Testa atualização de tarefa(PUT)
    atualizacao = {"tarefa": "Atualizada", "feito": True}
    response = client.put("/tarefas/1", json=atualizacao)

    assert response.status_code == 200
    dados = response.json
    assert dados["tarefa"] == "Atualizada"
    assert dados["feito"] is True

def test_atualizar_tarefa_inexistente(client):#Testa se a tarefa atualizada não existir gera erro
    atualizacao = {"tarefa": "Qualquer", "feito": True}
    response = client.put("/tarefas/9999", json=atualizacao)

    assert response.status_code == 404
    assert "erro" in response.json

def test_remover_tarefa_existente(client):#Testa se deleta tarefa (DELETE)
    response = client.delete("/tarefas/1")
    assert response.status_code == 200
    assert "mensagem" in response.json

    response_get = client.get("/tarefas/1")#Confirmando remoção
    assert response_get.status_code == 404

def test_remover_tarefa_inexistente(client):#Testa erro se a tarefa a ser deletada não ecxistir
    response = client.delete("/tarefas/9999")
    assert response.status_code == 404
    assert "erro" in response.json
